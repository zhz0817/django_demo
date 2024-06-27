# -*- coding: utf-8 -*-
from django.db import models


class Student(models.Model):
    sno = models.CharField(max_length=255, primary_key=True)  # 学号
    name = models.CharField(max_length=255)  # 姓名

    class Meta:
        db_table = "student"


class Subject(models.Model):  # 课程
    cname = models.CharField(max_length=255)  # 课程名

    class Meta:
        db_table = "subject"


class Grade(models.Model):
    sno = models.CharField(max_length=255)
    cno = models.CharField(max_length=255)
    score = models.IntegerField()

    class Meta:
        db_table = "grade"
