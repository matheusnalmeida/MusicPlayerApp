class User:

    def __init__(self, id: str, nome: str, usuario: str, senha: str) -> None:
        self.id = id
        self.nome = nome.strip()
        self.usuario = usuario.strip()
        self.senha = senha

    def is_valid(self) -> bool:
        id_filled = bool(self.id)
        nome_filled = bool(self.nome)
        usuario_filled = bool(self.usuario)
        senha_filled = bool(self.senha and self.senha.strip())
        
        return id_filled and nome_filled and usuario_filled and senha_filled