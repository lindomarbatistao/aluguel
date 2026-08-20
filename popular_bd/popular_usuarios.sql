SELECT * FROM aluguel.api_usuario;

INSERT INTO api_usuario (
    password, last_login, is_superuser, username, first_name, last_name,
    email, is_staff, is_active, date_joined, celular, tipo
) VALUES
('!', NULL, 0, 'joao.silva', 'João', 'Silva', 'joao.silva@email.com', 0, 1, NOW(), '19991234567', 'Usuario'),
('!', NULL, 0, 'maria.santos', 'Maria', 'Santos', 'maria.santos@email.com', 0, 1, NOW(), '19992345678', 'Usuario'),
('!', NULL, 0, 'carlos.oliveira', 'Carlos', 'Oliveira', 'carlos.oliveira@email.com', 0, 1, NOW(), '19993456789', 'Usuario'),
('!', NULL, 0, 'ana.souza', 'Ana', 'Souza', 'ana.souza@email.com', 0, 1, NOW(), '19994567890', 'Usuario'),
('!', NULL, 0, 'pedro.lima', 'Pedro', 'Lima', 'pedro.lima@email.com', 0, 1, NOW(), '19995678901', 'Usuario'),
('!', NULL, 0, 'juliana.costa', 'Juliana', 'Costa', 'juliana.costa@email.com', 0, 1, NOW(), '19996789012', 'Usuario'),
('!', NULL, 0, 'lucas.rocha', 'Lucas', 'Rocha', 'lucas.rocha@email.com', 0, 1, NOW(), '19997890123', 'Usuario'),
('!', NULL, 0, 'fernanda.alves', 'Fernanda', 'Alves', 'fernanda.alves@email.com', 0, 1, NOW(), '19998901234', 'Usuario'),
('!', NULL, 0, 'rafael.martins', 'Rafael', 'Martins', 'rafael.martins@email.com', 0, 1, NOW(), '19999012345', 'Usuario'),
('!', NULL, 0, 'patricia.ribeiro', 'Patrícia', 'Ribeiro', 'patricia.ribeiro@email.com', 0, 1, NOW(), '19990123456', 'Administrador');