from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Agent
from .forms import AgentForm

class AgentListView(ListView):
    model = Agent
    template_name = "gestion_agents/agent_list.html"
    context_object_name = "agents"
    paginate_by = 10  # Nombre d'agents par page

class AgentCreateView(CreateView):
    model = Agent
    form_class = AgentForm
    template_name = "gestion_agents/agent_form.html"
    success_url = reverse_lazy('agent-list')

class AgentUpdateView(UpdateView):
    model = Agent
    form_class = AgentForm
    template_name = "gestion_agents/agent_form.html"
    success_url = reverse_lazy('agent-list')

class AgentDeleteView(DeleteView):
    model = Agent
    template_name = "gestion_agents/agent_confirm_delete.html"
    success_url = reverse_lazy('agent-list')
