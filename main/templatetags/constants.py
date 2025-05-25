from django import template
from main.constants import STATIC_IMAGES, SOCIAL_LINKS, EXCHANGE_LINKS, CONTRACT_ADDRESS

register = template.Library()

@register.simple_tag
def get_static_image(key):
    """Получить путь к статическому изображению"""
    return STATIC_IMAGES.get(key, '')

@register.simple_tag
def get_social_link(key):
    """Получить ссылку на социальную сеть"""
    return SOCIAL_LINKS.get(key, '')

@register.simple_tag
def get_exchange_link(key):
    """Получить ссылку на биржу"""
    return EXCHANGE_LINKS.get(key, '')

@register.simple_tag
def get_contract_address():
    """Получить адрес контракта"""
    return CONTRACT_ADDRESS 