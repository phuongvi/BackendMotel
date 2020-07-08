from django.db import models

# Create your models here.
from django.utils import timezone

from user.models import User

# DISTRICT = (
#     ('Q01', 'Quận 1'),
#     ('Q02', 'Quận 2'),
#     ('Q03', 'Quận 3'),
#     ('Q04', 'Quận 4'),
#     ('Q05', 'Quận 5'),
#     ('Q06', 'Quận 6'),
#     ('Q07', 'Quận 7'),
#     ('Q08', 'Quận 8'),
#     ('Q09', 'Quận 9'),
#     ('Q10', 'Quận 10'),
#     ('Q11', 'Quận 11'),
#     ('Q12', 'Quận 12'),
#     ('BTA', 'Quận Bình Tân'),
#     ('BTH', 'Quận Bình Thạnh'),
#     ('QGV', 'Quận Gò Vấp'),
#     ('QPN', 'Quận Phú Nhuận'),
#     ('QTB', 'Quận Tân Bình'),
#     ('QTP', 'Quận Tân Phú'),
#     ('QTD', 'Quận Thủ Đức'),
#     ('HBC', 'Huyện Bình Chánh'),
#     ('HCG', 'Huyện Cần Giờ'),
#     ('HCC', 'Huyện Củ Chi'),
#     ('HHM', 'Huyện Hóc Môn'),
#     ('HNB', 'Huyện Nhà Bè'),
# )


DISTRICT = (
    ('1', 'Quận 1'),
    ('2', 'Quận 2'),
    ('3', 'Quận 3'),
    ('4', 'Quận 4'),
    ('5', 'Quận 5'),
    ('6', 'Quận 6'),
    ('7', 'Quận 7'),
    ('8', 'Quận 8'),
    ('9', 'Quận 9'),
    ('10', 'Quận 10'),
    ('11', 'Quận 11'),
    ('12', 'Quận 12'),
    ('13', 'Quận Bình Tân'),
    ('14', 'Quận Bình Thạnh'),
    ('15', 'Quận Gò Vấp'),
    ('16', 'Quận Phú Nhuận'),
    ('17', 'Quận Tân Bình'),
    ('18', 'Quận Tân Phú'),
    ('18', 'Quận Thủ Đức'),
    ('20', 'Huyện Bình Chánh'),
    ('21', 'Huyện Cần Giờ'),
    ('22', 'Huyện Củ Chi'),
    ('23', 'Huyện Hóc Môn'),
    ('24', 'Huyện Nhà Bè'),
)

MOTEL_TYPE = (
    ('A', 'Phòng Trọ'),
    ('B', 'Nhà Nguyên Căn'),
    ('C', 'Chung Cư'),
    ('D', 'Nhà Phố'),
    ('E', 'Nhà Ở Ghép')
)
class Motel(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)  # Tiêu đề bài viết
    content = models.TextField(null=True, blank=True)  # Nội dung bài viết
    typeMotel = models.CharField(max_length=1, choices=MOTEL_TYPE, default='A', db_index=True)  # Loại tin rao
    address = models.CharField(blank=True, max_length=255)  # Địa chỉ
    ward = models.CharField(blank=True, max_length=100)  # Phường
    district = models.CharField(max_length=3, choices=DISTRICT, default='1', db_index=True)  # Quận
    phone_number = models.CharField(blank=True, max_length=10)
    arc = models.PositiveIntegerField(blank=True, default=1)  # Diện tích
    price = models.PositiveIntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    def __str__(self):
        return self.title

class ImageMotel(models.Model):
    motel = models.ForeignKey(Motel, on_delete = models.CASCADE, related_name="motel")
    image = models.ImageField(upload_to = 'motel/')
    def __str__(self):
        return self.motel.title