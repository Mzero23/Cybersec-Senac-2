<?php
# LOCALIZA O PC COM O BANCO
$servidor = "localhost";
#NOME DO BANCO
$banco = "gov";
#USUARIO DO BANCO
$usuario = "root";
#SENHA
$senha = "";
#LINK PARA OUTRAS PAGINAS
$link = mysqli_connect($servidor, $usuario, $senha, $banco);
?>