BEGIN;

-- Insert 10 test users
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1000, '', NULL, false, 'user1000', 'User', 'One', 'user1@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1001, '', NULL, false, 'user1001', 'User', 'Two', 'user2@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1002, '', NULL, false, 'user1002', 'User', 'Three', 'user3@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1003, '', NULL, false, 'user1003', 'User', 'Four', 'user4@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1004, '', NULL, false, 'user1004', 'User', 'Five', 'user5@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1005, '', NULL, false, 'user1005', 'User', 'Six', 'user6@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1006, '', NULL, false, 'user1006', 'User', 'Seven', 'user7@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1007, '', NULL, false, 'user1007', 'User', 'Eight', 'user8@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1008, '', NULL, false, 'user1008', 'User', 'Nine', 'user9@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
   VALUES (1009, '', NULL, false, 'user1009', 'User', 'Ten', 'user10@example.com', false, true, NOW())
   ON CONFLICT (id) DO NOTHING;

-- Insert 30 sneaker listings (3 per user)
INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Air Retro', 'Nike', 9.5, 120.00, 'Classic silhouette in good condition.', 'images/nike1.png', 1000, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Court Zoom', 'Nike', 10.0, 85.00, 'Lightly used, clean soles.', 'images/nike2.png', 1000, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Classic Runner', 'Adidas', 9.0, 75.00, 'Everyday runner, comfortable.', 'images/adidas1.png', 1000, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Gel Lyte', 'ASICS', 8.5, 65.00, 'Minimal wear.', 'images/nike3.png', 1001, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Suede Classic', 'Puma', 9.0, 55.00, 'Retro look, good condition.', 'images/adidas2.png', 1001, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Trail Blazer', 'New Balance', 10.5, 95.00, 'Great for hiking.', 'images/newbalance1.png', 1001, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Street Low', 'Vans', 11.0, 40.00, 'Skate style, lightly used.', 'images/vans1.png', 1002, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Court Pro', 'Converse', 10.0, 30.00, 'Classic high-top look.', 'images/vans2.png', 1002, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Speed Trainer', 'Under Armour', 9.5, 70.00, 'Stable and supportive.', 'images/nike4.png', 1002, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Cushion Max', 'Brooks', 9.0, 80.00, 'Excellent cushioning for runs.', 'images/nike5.png', 1003, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Street Runner', 'Nike', 8.5, 110.00, 'Limited edition, good shape.', 'images/nike6.png', 1003, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Minimal Slip', 'Allbirds', 10.0, 95.00, 'Comfortable and eco-friendly.', 'images/adidas3.png', 1003, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Retro Pump', 'Reebok', 9.5, 60.00, 'Vintage style.', 'images/nike7.png', 1004, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Zoom Fly', 'Nike', 10.5, 150.00, 'Performance shoe, lightly used.', 'images/nike1.png', 1004, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('City Walk', 'Ecco', 9.0, 120.00, 'Premium comfort.', 'images/timbs1.png', 1004, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Court Ace', 'Nike', 8.0, 45.00, 'Stylish and clean.', 'images/nike2.png', 1005, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Lace Up', 'Adidas', 9.5, 85.00, 'Good for daily wear.', 'images/adidas1.png', 1005, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Runner Pro', 'Puma', 10.0, 65.00, 'Light running shoe.', 'images/adidas2.png', 1005, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Classic Low', 'Converse', 11.0, 35.00, 'Everyday casual.', 'images/vans1.png', 1006, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Flex Run', 'New Balance', 9.0, 90.00, 'Responsive midsole.', 'images/newbalance1.png', 1006, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Street Elite', 'Vans', 9.5, 50.00, 'Clean canvas look.', 'images/vans2.png', 1006, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Trail X', 'Salomon', 10.5, 130.00, 'Aggressive tread.', 'images/nike3.png', 1007, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Everyday Knit', 'Nike', 9.0, 99.00, 'Comfortable knit upper.', 'images/nike4.png', 1007, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Court Fresh', 'Adidas', 9.5, 70.00, 'Bright colorway.', 'images/adidas3.png', 1007, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Urban Slide', 'Birkenstock', 10.0, 80.00, 'Stylish sandal option.', 'images/timbs1.png', 1008, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Speed Knit', 'Under Armour', 8.5, 60.00, 'Light and breathable.', 'images/nike5.png', 1008, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Heritage Run', 'Brooks', 9.0, 75.00, 'Reliable and cushioned.', 'images/nike6.png', 1008, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Classic Knit', 'Allbirds', 9.5, 99.00, 'Sustainable material.', 'images/nike7.png', 1009, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Retro Pro', 'Reebok', 10.0, 55.00, 'Good collector piece.', 'images/adidas1.png', 1009, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

INSERT INTO marketplace_sneaker (name, brand, size, price, description, image, owner_id, created_at, updated_at, is_sold)
   VALUES ('Court Legend', 'Nike', 11.0, 140.00, 'Rare colourway.', 'images/nike1.png', 1009, NOW(), NOW(), false)
   ON CONFLICT DO NOTHING;

COMMIT;
