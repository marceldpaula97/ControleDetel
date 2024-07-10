from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QAction, QApplication, QDesktopWidget, \
    QPushButton, QMessageBox, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt

from main_window_button import MainWindowButtons
from register_product_window import RegisterProductWindow
from register_tecnico_window import RegisterTecnicoWindow
from register_fornecedores_window import RegisterFornecedorWindow
from print_handler import PrintHandler

class MainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.initUI(username)

    def initUI(self, username):
        # Saudação ao usuário
        label = QLabel(f'Bem-Vindo, {username}!', self)
        label.setAlignment(Qt.AlignCenter)  # Centraliza o texto horizontalmente
        label.setStyleSheet('font-size: 24px;')  # Define o tamanho da fonte

        layout = QVBoxLayout()
        layout.addWidget(label)

        # Botões para abrir as janelas de registro
        button_actions = MainWindowButtons(self)

        register_produto_button = QPushButton('Registrar Produto')
        register_produto_button.clicked.connect(self.open_register_product_window)
        layout.addWidget(register_produto_button)

        register_tecnico_button = QPushButton('Registrar Técnico')
        register_tecnico_button.clicked.connect(self.open_register_tecnico_window)
        layout.addWidget(register_tecnico_button)

        register_fornecedor_button = QPushButton('Registrar Fornecedor(a)')
        register_fornecedor_button.clicked.connect(self.open_register_fornecedor_window)
        layout.addWidget(register_fornecedor_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Menu de ações
        menu_bar = self.menuBar()

        # Ação de menu para imprimir
        print_action = QAction('Imprimir', self)
        print_action.triggered.connect(self.print_report)
        menu_bar.addAction(print_action)

        # Adicionar widget vazio para empurrar o botão de logout para a direita
        empty_widget = QWidget(self)
        empty_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        menu_bar.setCornerWidget(empty_widget, Qt.TopLeftCorner)

        # Botão de logout na barra de menu
        logout_button = QPushButton('Logout', self)
        logout_button.clicked.connect(self.confirm_logout)
        logout_button.setStyleSheet('padding: 5px 10px;')  # Customize a aparência do botão se necessário
        menu_bar.setCornerWidget(logout_button, Qt.TopRightCorner)

        self.setGeometry(0, 0, 800, 600)
        self.center()

    def confirm_logout(self):
        # Exibe uma mensagem de confirmação para o logout
        reply = QMessageBox.question(self, 'Confirmar Logout', 'Tem certeza que quer deslogar?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.logout()

    def logout(self):
        # Fecha a janela atual e abre a janela de login
        self.close()
        from login_window import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()

    def center(self):
        # Centraliza a janela na tela
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_register_tecnico_window(self):
        try:
            register_tecnico_window = RegisterTecnicoWindow()
            register_tecnico_window.exec_()
        except Exception as e:
            print(f'Erro ao abrir janela de registro de técnico: {e}')

    def open_register_product_window(self):
        try:
            register_product_window = RegisterProductWindow()
            register_product_window.exec_()
        except Exception as e:
            print(f'Erro ao abrir janela de registro de produto: {e}')

    def open_register_fornecedor_window(self):
        try:
            register_fornecedor_window = RegisterFornecedorWindow()
            register_fornecedor_window.exec_()
        except Exception as e:
            print(f'Erro ao abrir janela de registro de fornecedor: {e}')

    def print_report(self):
        print_handler = PrintHandler(self)
        print_handler.print_report()
