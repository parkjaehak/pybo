from django.db import models

class Product(models.Model):
    pd_name = models.CharField(max_length=20)
    pd_content = models.TextField(default='')
    pd_qty= models.IntegerField(default=0)
    pd_amt= models.IntegerField(default=0)
    create_date= models.DateTimeField()

    def __str__(self):
        dt_time = self.create_date.strftime('%Y-%m-%d %H:%M:%S')
        return '상품명=' + self.pd_name + ', ' + '수량=' + str(self.pd_qty) + ', ' + '금액=' + str(self.pd_amt) + ', ' + '일시=' \
            + str(dt_time)

