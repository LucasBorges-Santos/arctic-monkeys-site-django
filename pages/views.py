from django.views.generic import TemplateView
from django.shortcuts import render

# para views como classes
"""class sobre(TemplateView):
    template_name = 'sobre.html'

    # para indicar para a navbar qual pagina esta
    # coletar variaveis para integrar ao template
    def get_context_data(self, *args, **kwargs):
        context = {'pagina': 'sobre'}
        return context


class musicas(TemplateView):
    template_name = 'musicas.html'

    # para indicar para a navbar qual pagina esta
    # coletar variaveis para integrar ao template
    def get_context_data(self, *args, **kwargs):
        context = {'pagina': 'musicas'}
        return context"""


# para views como funcões
def sobre(request):
    template_name = 'sobre.html'

    # coletar variaveis para integrar ao template
    context = {'pagina': 'sobre'}

    return render(request, template_name, context=context)


def musicas(request):
    template_name = 'musicas.html'

    # coletar variaveis para integrar ao template
    context = {'pagina': 'musicas'}
    return render(request, template_name, context=context)
