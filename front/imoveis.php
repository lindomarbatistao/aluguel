<?php

$url = "http://127.0.0.1:8000/api/generics/imoveis/";

$json = file_get_contents($url);

$imoveis = json_decode($json, true);

?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Imóveis</title>
</head>

<body>
<h1>Lista de Imóveis</h1>

<?php foreach ($imoveis as $imovel) { ?>
    <h2><?= $imovel["titulo"] ?></h2>
    <p>Tipo: <?= $imovel["tipo"] ?></p>
    <p>Valor: R$ <?= $imovel["valor_aluguel"] ?></p>
    <p>Cidade: <?= $imovel["cidade"] ?></p>
    <hr>

<?php } ?>

</body>

</html>