# Generated by Django 3.2 on 2023-04-19 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='价格')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.SmallIntegerField(choices=[(1, '激活'), (0, '删除')], default=1, verbose_name='状态')),
                ('charge_type', models.SmallIntegerField(choices=[(1, '充值'), (2, '扣款'), (3, '创建订单'), (4, '删除订单'), (5, '撤单')], verbose_name='类型')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='金额')),
                ('order_oid', models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='订单号')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='交易时间')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.administrator', verbose_name='管理员')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.customer', verbose_name='客户')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.SmallIntegerField(choices=[(1, '激活'), (0, '删除')], default=1, verbose_name='状态')),
                ('status', models.SmallIntegerField(choices=[(1, '待执行'), (2, '正在执行'), (3, '已完成'), (4, '失败')], default=1, verbose_name='状态')),
                ('oid', models.CharField(max_length=64, unique=True, verbose_name='订单号')),
                ('url', models.URLField(db_index=True, verbose_name='视频地址')),
                ('count', models.IntegerField(verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='价格')),
                ('real_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='实际价格')),
                ('old_view_count', models.CharField(default='0', max_length=32, verbose_name='原播放量')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.customer', verbose_name='客户')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
