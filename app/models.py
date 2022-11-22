from django.db import models
from base.models import BaseModel
from authentication.models import StudentModel


class CompanyModel(BaseModel):
    company_name = models.CharField(max_length=50)
    address = models.TextField()
    web_link = models.URLField(max_length=200)
    def __str__(self):
        return self.company_name
    class Meta:
        db_table = "company"


class JobModel(BaseModel):
    position = models.CharField(max_length=50)
    company = models.ForeignKey(CompanyModel, related_name="company_job_listing", on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    pay_rate = models.PositiveIntegerField()
    max_applicant = models.PositiveSmallIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.position
    class Meta:
        db_table = "job"


class JobApplication(BaseModel):
    job = models.ForeignKey(JobModel, related_name="job_applied", on_delete=models.CASCADE)
    applicant = models.ForeignKey(StudentModel, related_name="job_applicant", on_delete=models.CASCADE)
    def __str__(self):
        return self.job.posting
    class Meta:
        db_table = "job_application"
