from django.db import models

# Create your models here.
"""
# 모델을 다음과 같이 작성하고 db에서 load를 해야한다.
# 프로젝트 진행 당시엔 당장 구현이 급해 놓치고 넘어갔던 부분

class Trashcans(models.Model):
    borough = models.CharField(max_length=20)   # 구 이름
    street = models.CharField(max_length=20)    # 도로명
    location = models.CharField(max_length=200) # 설치장소상세
    latitude = models.DecimalField(max_digits=9, decimal_places=6)     # 위도
    longitude = models.DecimalField(max_digits=9, decimal_places=6)    # 경도
"""
