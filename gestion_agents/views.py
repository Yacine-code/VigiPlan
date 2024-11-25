from django.urls import reverse_lazy  # Utilisé pour générer des URL basées sur le nom des routes
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # Importation des vues génériques
from .models import Agent  # Importation du modèle Agent
from .forms import AgentForm  # Importation du formulaire personnalisé

# Vue pour afficher la liste des agents
class AgentListView(ListView):
    model = Agent  # Modèle à utiliser
    template_name = "gestion_agents/agent_list.html"  # Template HTML à rendre
    context_object_name = "agents"  # Nom du contexte passé au template
    paginate_by = 10  # Pagination : 10 agents par page

# Vue pour créer un nouvel agent
class AgentCreateView(CreateView):
    model = Agent
    form_class = AgentForm  # Utilisation du formulaire personnalisé
    template_name = "gestion_agents/agent_form.html"  # Template HTML pour le formulaire
    success_url = reverse_lazy('agent-list')  # Redirection en cas de succès

# Vue pour mettre à jour un agent existant
class AgentUpdateView(UpdateView):
    model = Agent
    form_class = AgentForm
    template_name = "gestion_agents/agent_form.html"
    success_url = reverse_lazy('agent-list')

# Vue pour supprimer un agent
class AgentDeleteView(DeleteView):
    model = Agent
    template_name = "gestion_agents/agent_confirm_delete.html"  # Template HTML pour confirmer la suppression
    success_url = reverse_lazy('agent-list')
