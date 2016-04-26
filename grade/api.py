from .models import Rule, Grade, Log
from wechat_member.models import Member

class GradeApi(object):
    'grade api'

    def __init__(self, member_id):
        member = self.get_member(member_id)
        if not member:
            return None
        self.member = member
        self.grade = self.get_grade()


    """
    check member is not exist
    """
    def get_member(self, member_id):
        try:
            member = Member.objects.get(id=member_id)
            return member
        except Member.DoesNotExist:
            return None

    """
    get member' grade
    is not exist, create it
    """
    def get_grade(self):
        try:
            grade = Grade.objects.get(member=self.member)
        except Grade.DoesNotExist:
            grade = self.create_grade()
        return grade


    """
    create new member grade
    """
    def create_grade(self):
        min_rule = Rule.objects.order_by('growth').first()
        grade = Grade.objects.create(
            member = self.member,
            grade = min_rule,
            growth = 0,
        )
        return grade


    """
    get log list
    """
    def get_log(self, offset=0, length=10):
        return Log.objects.filter(member=self.grade)\
                          .order_by('-created')[offset:length]

    """
    increase or reduce log
    """
    def add_log(self, log_type, value, description):
        if log_type not in ['increase', 'reduce']:
            return False
        elif type(value) is not int:
            return False
        elif value <= 0:
            return False
        elif not description:
            return False

        print 'add log starting...'
        Log.objects.create(
            member = self.grade,
            type = log_type,
            value = value,
            description = description,
        )
        print 'add log end'

        if log_type == 'increase':
            self.grade.growth += value
        else:
            self.grade.growth -= value
        self.grade.save()
        self.check_grade()
        return True


    """
    check is member's grade been grow
    """
    def check_grade(self):
        print 'check grade starting...'
        growth = self.grade.growth
        rule = Rule.objects.filter(growth__lte=growth)\
               .order_by('-growth').first()
        if rule.id != self.grade.grade.id:
            print 'your grade is changed'
            self.grade.grade = rule
            self.grade.save()
            self.push_message()
        print 'check grade end'
        return rule



    """
    push message for grade grow
    """
    def push_message(self):
        print 'your grade is changed'
