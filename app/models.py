from django.db import models


class HeaderText (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Text"


class FooterText(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"


class TreeBlocks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="tree-blocks")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tree Block"
        verbose_name_plural = "Tree Blocks"


class LeftBlock(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="left-block")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Left Block"
        verbose_name_plural = "Left Block"


class RightBlock(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="right-block")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Right Block"
        verbose_name_plural = "Right Block"


class WorkProcessMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Work Process"
        verbose_name_plural = "Work Process"


class WorkProcessChild(models.Model):
    parent = models.ForeignKey(
        WorkProcessMain, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="work-process")

    def __str__(self):
        return self.title
