-- Seed file for SneakerHub (SQLite)
-- Creates 10 users (ids 1000-1009) and 30 sneaker listings owned by those users.

PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;

-- Insert 10 test users
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1000, '', NULL, 0, 'user1000', 'User', 'One', 'user1@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1001, '', NULL, 0, 'user1001', 'User', 'Two', 'user2@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1002, '', NULL, 0, 'user1002', 'User', 'Three', 'user3@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1003, '', NULL, 0, 'user1003', 'User', 'Four', 'user4@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1004, '', NULL, 0, 'user1004', 'User', 'Five', 'user5@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1005, '', NULL, 0, 'user1005', 'User', 'Six', 'user6@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1006, '', NULL, 0, 'user1006', 'User', 'Seven', 'user7@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1007, '', NULL, 0, 'user1007', 'User', 'Eight', 'user8@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1008, '', NULL, 0, 'user1008', 'User', 'Nine', 'user9@example.com', 0, 1, CURRENT_TIMESTAMP);
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1009, '', NULL, 0, 'user1009', 'User', 'Ten', 'user10@example.com', 0, 1, CURRENT_TIMESTAMP);

-- Insert 30 sneaker listings (3 per user)
-- Columns: name, brand, size, price, description, image, owner_id, created_at, updated_at

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Air Retro', 'Nike', 9.5, 120.00, 'Classic silhouette in good condition.', NULL, 1000, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Court Zoom', 'Nike', 10.0, 85.00, 'Lightly used, clean soles.', NULL, 1000, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Classic Runner', 'Adidas', 9.0, 75.00, 'Everyday runner, comfortable.', NULL, 1000, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Gel Lyte', 'ASICS', 8.5, 65.00, 'Minimal wear.', NULL, 1001, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Suede Classic', 'Puma', 9.0, 55.00, 'Retro look, good condition.', NULL, 1001, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Trail Blazer', 'New Balance', 10.5, 95.00, 'Great for hiking.', NULL, 1001, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Street Low', 'Vans', 11.0, 40.00, 'Skate style, lightly used.', NULL, 1002, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Court Pro', 'Converse', 10.0, 30.00, 'Classic high-top look.', NULL, 1002, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Speed Trainer', 'Under Armour', 9.5, 70.00, 'Stable and supportive.', NULL, 1002, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Cushion Max', 'Brooks', 9.0, 80.00, 'Excellent cushioning for runs.', NULL, 1003, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Street Runner', 'Nike', 8.5, 110.00, 'Limited edition, good shape.', NULL, 1003, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Minimal Slip', 'Allbirds', 10.0, 95.00, 'Comfortable and eco-friendly.', NULL, 1003, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Retro Pump', 'Reebok', 9.5, 60.00, 'Vintage style.', NULL, 1004, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Zoom Fly', 'Nike', 10.5, 150.00, 'Performance shoe, lightly used.', NULL, 1004, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('City Walk', 'Ecco', 9.0, 120.00, 'Premium comfort.', NULL, 1004, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Court Ace', 'Nike', 8.0, 45.00, 'Stylish and clean.', NULL, 1005, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Lace Up', 'Adidas', 9.5, 85.00, 'Good for daily wear.', NULL, 1005, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Runner Pro', 'Puma', 10.0, 65.00, 'Light running shoe.', NULL, 1005, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Classic Low', 'Converse', 11.0, 35.00, 'Everyday casual.', NULL, 1006, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Flex Run', 'New Balance', 9.0, 90.00, 'Responsive midsole.', NULL, 1006, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Street Elite', 'Vans', 9.5, 50.00, 'Clean canvas look.', NULL, 1006, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Trail X', 'Salomon', 10.5, 130.00, 'Aggressive tread.', NULL, 1007, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Everyday Knit', 'Nike', 9.0, 99.00, 'Comfortable knit upper.', NULL, 1007, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Court Fresh', 'Adidas', 9.5, 70.00, 'Bright colorway.', NULL, 1007, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Urban Slide', 'Birkenstock', 10.0, 80.00, 'Stylish sandal option.', NULL, 1008, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Speed Knit', 'Under Armour', 8.5, 60.00, 'Light and breathable.', NULL, 1008, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Heritage Run', 'Brooks', 9.0, 75.00, 'Reliable and cushioned.', NULL, 1008, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Classic Knit', 'Allbirds', 9.5, 99.00, 'Sustainable material.', NULL, 1009, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Retro Pro', 'Reebok', 10.0, 55.00, 'Good collector piece.', NULL, 1009, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at) VALUES ('Court Legend', 'Nike', 11.0, 140.00, 'Rare colourway.', NULL, 1009, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

COMMIT;
PRAGMA foreign_keys = ON;