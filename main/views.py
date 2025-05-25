from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Представление для главной страницы
    """
    return render(request, 'main/index.html')

def about(request):
    """
    Представление для страницы "О нас"
    """
    return render(request, 'main/about.html')

def buy(request):
    """
    Представление для страницы покупки токенов
    """
    # Список доступных бирж и DEX
    exchanges = [
        {
            'name': 'PancakeSwap',
            'url': 'https://pancakeswap.finance/',
            'description': 'Scambia VATIC su BNB Smart Chain',
            'icon': 'pancakeswap.png'
        },
        {
            'name': 'Uniswap',
            'url': 'https://uniswap.org/',
            'description': 'Scambia VATIC su Ethereum',
            'icon': 'uniswap.png'
        },
        {
            'name': 'CoinGecko',
            'url': 'https://www.coingecko.com/',
            'description': 'Traccia il prezzo di VATIC',
            'icon': 'coingecko.png'
        }
    ]
    
    context = {
        'exchanges': exchanges
    }
    return render(request, 'main/buy.html', context)

def contact(request):
    """
    Представление для страницы контактов
    """
    return render(request, 'main/contact.html')

def minigame(request):
    return render(request, 'main/minigame.html')
