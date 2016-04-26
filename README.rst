基于django_wechat_member的会员等级模块
=======================================

一个基于 `django_wechat_member <http://github.com/ChanMo/django_wechat_member/>`_ 的会员等级模块

功能说明：
----------

- 会员等级名称及排序
- 会员等级的临界成长值
- 成长值的记录
- api接口

快速开始:
---------

安装 *django_wechat_member* :

    `有关django_wechat_member的详细使用说明 <http://github.com/ChanMo/django_wechat_member.git/>`_ 

修改 *settings.py* 文件:

.. code-block::

    INSTALLED_APPS = (
        ...
        'grade',
        ...
    )

更新数据库:

.. code-block::

   python manage.py migrate


版本更改:
---------
- v0.1 第一版
