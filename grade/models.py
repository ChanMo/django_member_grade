#!/usr/bin/python
# vim: set fileencoding=utf-8 :
from __future__ import unicode_literals
from django.db import models
from wechat_member.models import Member

class Rule(models.Model):
    '等级规则'
    name = models.CharField(max_length=200, verbose_name='名称')
    value = models.CharField(max_length=200, verbose_name='值')
    growth = models.IntegerField(verbose_name='临界成长值')
    def __unicode__(self):
        return self.name

    class Meta(object):
        ordering = ['-growth']
        verbose_name = '等级规则'
        verbose_name_plural = '等级规则'


class Grade(models.Model):
    '会员等级'
    member = models.OneToOneField(Member, related_name='grade', verbose_name='会员')
    grade = models.ForeignKey(Rule, related_name='members', verbose_name='等级')
    growth = models.IntegerField(default=0, verbose_name='成长值')
    def __unicode__(self):
        return self.member.name

    class Meta(object):
        verbose_name = '会员等级'
        verbose_name_plural = '会员等级'


class Log(models.Model):
    '成长记录'
    TYPE_CHOICES = (
        ('increase', '增加'),
        ('reduce', '减少'),
    )
    member = models.ForeignKey(Grade, related_name='grade_log', verbose_name='会员')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name='类型')
    value = models.IntegerField(verbose_name='成长值')
    description = models.CharField(max_length=255, verbose_name='描述')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    def __unicode__(self):
        return self.description

    class Meta(object):
        verbose_name = '成长记录'
        verbose_name_plural = '成长记录'
