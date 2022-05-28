import time
from PIL import Image

def highlight(element, arquivo):
    effect_time= 5
    color='red'
    border=3  
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)

    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    driver.save_screenshot(f'/home/pedromattos/Documentos/Linkedin/exemplo_selenium_python/selenium_python_ex/evidencias/{arquivo}.png')  
    apply_style(original_style)

def dados_conta() -> dict:
    cadastro={'email1': 'contaA@bugbank.com',
                'email2': 'contaB@bugbank.com',
                'nome': 'pedro mattos',
                'senha':  '123m'}
    return cadastro