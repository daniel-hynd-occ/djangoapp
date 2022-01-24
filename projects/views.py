from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from projects.forms import DatabaseBuilderForm, ProjectForm, VariableExtractionForm, VariableSetForm

from .models import Project, VariableExtraction, VariableSet

@login_required
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', { 'projects': projects })

@login_required
def create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    
    else:
        form = ProjectForm(label_suffix=":")
        user_list = User.objects.all()
        return render(request, 'create.html', {'form': form, 'user_list': user_list})

@login_required
def update(request, id):
    project = get_object_or_404(Project, pk=id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('details', kwargs={'id': id}))
    
    else:
        name = project.name
        form = ProjectForm(instance=project)
        return render(request, 'update.html', {'form': form, 'name': name, 'id': id})

@login_required
def details(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'details.html', {'project': project})

@login_required
def delete(request, id):
    get_object_or_404(Project, pk=id).delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
def variable_sets(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'variable-sets.html', {'project': project, 'variable_sets': project.variable_sets.all()})

@login_required
def variable_set_create(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        form = VariableSetForm(request.POST)
        if form.is_valid():
            variable_set = form.save(commit=False)
            variable_set.project = project
            variable_set.save()
        return HttpResponseRedirect(reverse('variable-sets', kwargs={'id': id}))

    else:
        form = VariableSetForm(label_suffix="")
        return render(request, 'variable-set-create.html', {'project': project, 'form': form})

@login_required
def database_builder(request, id):
    project = get_object_or_404(Project, pk=id)

    if request.method == 'POST':
        form = DatabaseBuilderForm(request.POST)
        if(form.is_valid()):
            if(project.database_builder_state == Project.DatabaseBuilderState.NOT_STARTED):
                project.input_directory = form.data['input_directory']
                project.database_builder_state = Project.DatabaseBuilderState.RUNNING
                project.save()
            elif(project.database_builder_state == Project.DatabaseBuilderState.RUNNING):
                project.database_builder_state = Project.DatabaseBuilderState.NOT_STARTED
                project.save()
            return HttpResponseRedirect(reverse('database-builder', kwargs={'id': id}))

    else:
        return render(request, 'database-builder.html', {'project': project})

@login_required
def variable_set_details(request, id, variable_set_id):
    variable_set = get_object_or_404(VariableSet, pk=variable_set_id)
    return render(request, 'variable-set-details.html', {'variable_set': variable_set, 'project': variable_set.project})

@login_required
def variable_extractions(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'variable-extractions.html', {'project': project, 'variable_extractions': project.variable_extractions.all()})

@login_required
def variable_extraction_create(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        form = VariableExtractionForm(request.POST)
        if form.is_valid():
            variable_extraction = form.save(commit=False)
            variable_extraction.project = project
            variable_extraction.state = VariableExtraction.VariableExtractionState.NOT_STARTED
            variable_extraction.save()
        return HttpResponseRedirect(reverse('variable-extractions', kwargs={'id': id}))

    else:
        form = VariableExtractionForm(label_suffix="")
        return render(request, 'variable-extraction-create.html', {'project': project, 'form': form})

@login_required
def variable_extraction_details(request, id, variable_extraction_id):
    variable_extraction = get_object_or_404(VariableExtraction, pk=variable_extraction_id)
    
    if request.method == 'POST':
        if(variable_extraction.state == VariableExtraction.VariableExtractionState.NOT_STARTED):
            variable_extraction.state = VariableExtraction.VariableExtractionState.RUNNING
            variable_extraction.save()
        elif(variable_extraction.state == VariableExtraction.VariableExtractionState.RUNNING):
            variable_extraction.state = VariableExtraction.VariableExtractionState.NOT_STARTED
            variable_extraction.save()
        return HttpResponseRedirect(reverse('variable-extraction-details', kwargs={'id': id, 'variable_extraction_id': variable_extraction_id}))

    else:
        return render(request, 'variable-extraction-details.html', {'variable_extraction': variable_extraction, 'project': variable_extraction.project})