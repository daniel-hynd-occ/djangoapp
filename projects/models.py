from django.db import models

class Project(models.Model):

    class DatabaseBuilderState(models.IntegerChoices):
        NOT_STARTED = 0
        RUNNING = 1
        COMPLETE = 2

    isac_protocol = models.CharField(max_length=256)
    isac_approved = models.BooleanField()
    name = models.CharField(max_length=256)
    protocol_title = models.CharField(max_length=1024)
    date_created = models.DateTimeField(auto_now_add=True)
    database_builder_state = models.IntegerField(
        choices=DatabaseBuilderState.choices, 
        default=DatabaseBuilderState.NOT_STARTED
    )
    input_directory = models.CharField(max_length=1024)

class VariableSet(models.Model):
    name = models.CharField(max_length=256)
    index_date = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="variable_sets")
    def __str__(self):
            return self.name

class VariableExtraction(models.Model):

    class VariableExtractionState(models.IntegerChoices):
        NOT_STARTED = 0
        RUNNING = 1
        COMPLETE = 2

    name = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="variable_extractions")
    variable_set = models.ForeignKey(VariableSet, on_delete=models.CASCADE, related_name="variable_extractions")
    state = models.IntegerField(
        choices=VariableExtractionState.choices,
        default=VariableExtractionState.NOT_STARTED
    )