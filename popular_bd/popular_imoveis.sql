USE aluguel;

SELECT * FROM aluguel.api_imovel;

INSERT INTO api_imovel (
    titulo, tipo, valor_aluguel, status, logradouro, cep, complemento, bairro, cidade, uf
) VALUES
('Casa com 3 dormitórios', 'casa', 2500.00, 1, 'Rua das Flores, 150', '13140000', 'Próximo ao supermercado', 'Jardim das Palmeiras', 'Campinas', 'SP'),
('Apartamento com 2 dormitórios', 'apartamento', 1800.00, 1, 'Avenida Brasil, 850', '13070000', 'Apartamento 42', 'Jardim Guanabara', 'Campinas', 'SP'),
('Casa com 2 dormitórios', 'casa', 1950.00, 1, 'Rua dos Ipês, 320', '13058000', NULL, 'Jardim Aurélia', 'Campinas', 'SP'),
('Apartamento próximo ao centro', 'apartamento', 2200.00, 1, 'Rua Barreto Leme, 725', '13010000', 'Apartamento 81', 'Centro', 'Campinas', 'SP'),
('Kitnet mobiliada', 'kitnet', 1200.00, 1, 'Rua Culto à Ciência, 410', '13020060', 'Fundos', 'Botafogo', 'Campinas', 'SP'),
('Casa com garagem', 'casa', 2800.00, 1, 'Rua das Acácias, 95', '13087000', 'Garagem para 2 carros', 'Barão Geraldo', 'Campinas', 'SP'),
('Apartamento com 3 dormitórios', 'apartamento', 3200.00, 1, 'Avenida Norte Sul, 1200', '13025000', 'Apartamento 102', 'Cambuí', 'Campinas', 'SP'),
('Kitnet próxima à universidade', 'kitnet', 1350.00, 1, 'Rua José Martins, 240', '13084000', NULL, 'Barão Geraldo', 'Campinas', 'SP'),
('Casa com quintal', 'casa', 2100.00, 0, 'Rua das Laranjeiras, 580', '13060000', 'Casa 2', 'Jardim Chapadão', 'Campinas', 'SP'),
('Apartamento com varanda', 'apartamento', 2650.00, 1, 'Rua Maria Monteiro, 630', '13025000', 'Apartamento 73', 'Cambuí', 'Campinas', 'SP');