__all__ = ['create_membro', 'get_membros', 'get_membro_by_id', 'set_funcoes', 'delete_membro']

# Variaveis globais
lista_membros = list()

# Códigos de erro
OPERACAO_REALIZADA_COM_SUCESSO = 0
EQUIPE_NAO_ENCONTRADA = 1
MEMBRO_NAO_ENCONTRADO = 2

# Funções


def create_membro(nome: str, funcoes: list) -> tuple[int, dict]:
    global lista_membros

    membro = {
        "id": len(lista_membros) + 1,
        "nome": nome,
        "funcoes": funcoes
    }

    lista_membros.append(membro)
    return OPERACAO_REALIZADA_COM_SUCESSO, membro


def get_membros() -> tuple[int, list]:
    global lista_membros
    return OPERACAO_REALIZADA_COM_SUCESSO, lista_membros


def get_membro_by_id(id_membro: int) -> tuple[int, dict]:
    global lista_membros

    for membro in lista_membros:
        if membro["id"] == id_membro:
            return OPERACAO_REALIZADA_COM_SUCESSO, membro

    return MEMBRO_NAO_ENCONTRADO, []


def set_funcoes(id_membro: int, funcoes: list) -> tuple[int, dict]:
    global lista_membros

    for membro in lista_membros:
        if membro["id"] == id_membro:
            membro["funcoes"] = funcoes
            return OPERACAO_REALIZADA_COM_SUCESSO, membro

    return MEMBRO_NAO_ENCONTRADO, []


def delete_membro(id_membro: int) -> tuple[int, dict]:
    global lista_membros

    for membro in lista_membros:
        if membro["id"] == id_membro:
            lista_membros.remove(membro)
            return OPERACAO_REALIZADA_COM_SUCESSO, membro

    return MEMBRO_NAO_ENCONTRADO, []
