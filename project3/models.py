from django.db import models

# Create your models here.
class data(models.Model):
    id = models.BigIntegerField(primary_key=True)
    summoners = models.CharField(max_length=255)
    game = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    champion = models.TextField()
    level = models.IntegerField()
    d_spell = models.TextField()
    f_spell = models.TextField()
    main_rune = models.TextField()
    sub_rune = models.TextField()
    items = models.TextField()
    kill = models.IntegerField()
    death = models.IntegerField()
    assist = models.IntegerField()
    p_kill = models.CharField(max_length=255)
    pinkward = models.IntegerField()
    cs = models.IntegerField()
    cs_per_min = models.IntegerField()
    average_tier = models.CharField(max_length=255)
    team_champs = models.TextField()
    team = models.TextField()
    enemy_champs = models.TextField()
    enemy = models.TextField()
    side = models.CharField(max_length=255)

    class Meta:
        db_table = 'data'