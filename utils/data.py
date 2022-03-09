import json


def countVaiant(listVariant):
    retorno = {}
    totalVariantsEncontradas=[]
    variantesAgrupadas = []

    for element in listVariant:
        if element not in totalVariantsEncontradas:
            totalVariantsEncontradas.append(element)
    retorno['TotalVariantesEncontrado'] = len(totalVariantsEncontradas)

    for elemente in totalVariantsEncontradas:
        dictVariantesAgrupadas={}
        dictVariantesAgrupadas['variant']=elemente
        dictVariantesAgrupadas['TotalOcorrencias']=listVariant.count(element)
        variantesAgrupadas.append(dictVariantesAgrupadas)
    retorno['TotalCasosPorVariante']=variantesAgrupadas

    return retorno



def montaJson(informacoes,dictVariantes):
    jsonReturn={}
    jsonReturn['informacoes']=informacoes
    jsonReturn['totalCasosConfirmado']=dictVariantes['totalCasosConfirmado']
    jsonReturn['totalCasosPorVariante']=dictVariantes['totalCasosPorVariante']
    jsonReturn['retorno']=dictVariantes['retorno']
    return jsonReturn
    