
INSERT INTO Account_User (username, password, email) VALUES ('Heiðar Sigurjónsson', '$2y$12$fVXw/5lDzOdt8Qb2pv4C7eTbHkoPW0.Y3/ZsAC6swykRezwQxvHGW', 'heidars19@ru.is');
INSERT INTO Account_User (username, password, email) VALUES ('Snæbjörg Pétursdóttir', '$2y$12$fVXw/5lDzOdt8Qb2pv4C7eTbHkoPW0.Y3/ZsAC6swykRezwQxvHGW', 'snaebjorg19@ru.is');
INSERT INTO Account_User (username, password, email) VALUES ('Helga Árnadóttir', '$2y$12$fVXw/5lDzOdt8Qb2pv4C7eTbHkoPW0.Y3/ZsAC6swykRezwQxvHGW', 'helgaa19@ru.is');
INSERT INTO Account_User (username, password, email) VALUES ('Alexander Freyr Lúðvíksson', 'hiuÐEhiueoiðewhuwLBHWLBSbslsbudL', 'alexanderl17@ru.is');
INSERT INTO Account_User (username, password, email) VALUES ('Eyþór Óli Borgþórsson', '$2y$12$fVXw/5lDzOdt8Qb2pv4C7eTbHkoPW0.Y3/ZsAC6swykRezwQxvHGW', 'eythorb19@ru.is');


INSERT INTO Account_PaymentInfo (user_id_id, name, exp_date, card_number, cvc) VALUES (1, 'Heiðar Sigurjónsson', '24-03', '394488727712', '123');
INSERT INTO Account_PaymentInfo (user_id_id, name, exp_date, card_number, cvc) VALUES (2, 'Snæbjörg Pétursdóttir', '20-08', '789356733451', '321');
INSERT INTO Account_PaymentInfo (user_id_id, name, exp_date, card_number, cvc) VALUES (3, 'Helga Árnadóttir', '26-09', '394488727712', '456');
INSERT INTO Account_PaymentInfo (user_id_id, name, exp_date, card_number, cvc) VALUES (5, 'Eyþór Óli Borgþórsson', '22-12', '394488720000', '654');
INSERT INTO Account_PaymentInfo (user_id_id, name, exp_date, card_number, cvc) VALUES (4, 'Alexander Freyr Lúðvíksson', '21-01', '000088727712', '789');


INSERT INTO Account_Address (user_id_id, address, city, country, zip_code) VALUES (1, 'Beykidal 6, 204', 'Njarðvík', 'Iceland', '321');
INSERT INTO Account_Address (user_id_id, address, city, country, zip_code) VALUES (2, 'Reynisgötu 12', 'Moskva', 'Rússland', '923817');
INSERT INTO Account_Address (user_id_id, address, city, country, zip_code) VALUES (3, 'Öldutúni 192', 'Reykjavík', 'Iceland', '101');
INSERT INTO Account_Address (user_id_id, address, city, country, zip_code) VALUES (4, 'Helli númer 3', 'Reykjavík', 'Iceland', '1101');
INSERT INTO Account_Address (user_id_id, address, city, country, zip_code) VALUES (5, 'Elliðadal 1', 'Hafnarfirði', 'Iceland', '121');


INSERT INTO Account_UserPhoto (user_id_id, path, alt) VALUES ('1', 'https://photos.alexfreyr.com/profilemynd1.jpg', 'Heiðar');
INSERT INTO Account_UserPhoto (user_id_id, path, alt) VALUES ('2', 'https://photos.alexfreyr.com/profilemynd2.jpg', 'Snæbjörg');
INSERT INTO Account_UserPhoto (user_id_id, path, alt) VALUES ('3', 'https://photos.alexfreyr.com/profilemynd3.jpg', 'Helga');
INSERT INTO Account_UserPhoto (user_id_id, path, alt) VALUES ('4', 'https://photos.alexfreyr.com/profilemynd4.jpg', 'Alexander');
INSERT INTO Account_UserPhoto (user_id_id, path, alt) VALUES ('5', 'https://photos.alexfreyr.com/profilemynd5.jpg', 'Eyþór');


INSERT INTO store_category (name) VALUES ('Games')
INSERT INTO store_category (name) VALUES ('Console')
INSERT INTO store_category (name) VALUES ('Other')


INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('Donkey Kong 64', 23.55, 50, 5, 1);
INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('Legend of Zelda', 13.98, 13.5, 2, 1);
INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('Super Mario 64', 29.99, 0, 213, 1);
INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('The Shadow of the Beast III', 9.89, 0, 0, 1);
INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('Sonic the Hedgehog 2', 12.30, 5, 2, 1);
INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('Turrican', 9.30, 0, 1, 1);

INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('Super NES Classic', 79.99, 5, 6, 2);
INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('SEGA Genesis / Mega Drive Mini', 19.89, 0, 0, 2);
INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('Atari Flashback 8 Gold Deluxe', 19.30, 10, 1, 2);
INSERT INTO Store_Product (name, price, discount, copies_sold, category_id) VALUES ('PlayStation Classic', 99.99, 5, 2, 2);


INSERT INTO Store_Genre (genre) VALUES ('First Person Shooter');
INSERT INTO Store_Genre (genre) VALUES ('Adventure');
INSERT INTO Store_Genre (genre) VALUES ('Arcade');
INSERT INTO Store_Genre (genre) VALUES ('RPG');
INSERT INTO Store_Genre (genre) VALUES ('Platform');


INSERT INTO Store_Developer (developer) VALUES ('Nintendo PTD');
INSERT INTO Store_Developer (developer) VALUES ('Sony');
INSERT INTO Store_Developer (developer) VALUES ('Sega');
INSERT INTO Store_Developer (developer) VALUES ('Amiga');
INSERT INTO Store_Developer (developer) VALUES ('Commadore 64');
INSERT INTO Store_Developer (developer) VALUES ('Legacy Engineering');


INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 1, 3, 1, '1999-11-22',
    'This 1999 classic is the first Donkey Kong game to feature 3D gameplay. It`s up to you, Donkey Kong, to rescue your kidnapped friends from King K. Rool. Use your special abilities to overcome obstacles and receive all kinds of collectibles along the way. Last man standing and deathmatch games are available in multiplayer mode, where up to four players can compete.');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 2, 2, 1, '1986-2-21',
    'Join Link on his journey, as he tries to defeat the dark lord Ganon, save Hyrule and rescue the descendants of the Seven Sages. Get familiar with the Master Sword and parallel worlds as you embark on this adventure.');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 3, 4, 1, '1996-6-23',
    'It`s Super Mario to the rescue when Princess Peach is kidnapped by the malicious Bowser. Run through Peach`s castle and overcome obstacles and fight off enemies in order to save Peach. This outstanding game takes you on a journey like no other!');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 4, 3, 4, '1992-1-1',
    'Aarbron has reclaimed his human shape, nevertheless, he hasn`t completely liberated himself from evil Maletoth`s curse. You, as Aarbron, must solve problems and collect four special items, with the aim of becoming powerful enough to face Maletoth and vanquish him once and for all!');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 5, 4, 3, '1992-11-21',
    'In this classic game, Sonic and his good friend and sidekick, Tails, have to use their powers and strengths to fight the evil Dr. Eggman. Run and fly with Sonic and Tails on their journey to destroy Dr. Eggman`s wicked plans and rescue the kidnapped animals!');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 6, 1, 5, '1990-1-1',
    'Morgul, the three-headed demon, has been causing everyone in the galaxy terrible nightmares. It`s up to you, Turrican, to find and defeat Morgul. On your journey to save the galaxy, you can  come across many different weapons that you can collect and use to help you on your quest. People are terrified of sleeping and some are even at death`s door as a result of exhaustion. Only you can rescue the people and put an end to this misery.');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 7, 5, 1, '2017-6-26',
    'Apart from being a lot smaller, the Super NES Classic looks like the original console and certainly has the same feel. It has 21 pre-installed games and two consoles, which allows you and your friends to indulge in some of the best 2-player games of the era!');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 8, 5, 3, '1988-10-29',
    'This ultra-lightweight, Genesis Mini, presents 42 games and is very simple in use. There are solely two ports on the back, for HDMI and power. The Genesis Mini is actually a quite accurate recreation of the original hardware. It has detailed features that serve a nostalgic purpose, more so than an actual functional purpose. The simplicity of Genesis Mini is definitely what sets it apart from the modern devices that regularly  require online updates. Very straightforward controller.');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 9, 5, 6, '2004-11-21',
    '120 games are available in this edition. This comes with an easy-to-use system, a save, pause, and rewind feature and scan line filtering. There are legacy controller ports for facultative joysticks or paddles with wires. You will get the Atari Flashback 8 Gold Console, along with one set of paddle controllers and 2 wireless controllers. You will also receive an HDMI Cable, as there is an 720p HDMI output. Enjoy this great recreation!');
INSERT INTO Store_ProductDetails (product_id_id, genre_id_id, developer_id_id, release_date, description) VALUES ( 10, 5, 2, '2018-1-1',
    'This recreation of the classic PlayStation, captures the magic of the golden era. Apart from the size difference, the recreation is almost identical to the original. Despite being 45% smaller than the original, it comes with two of the iconic controllers, a virtual memory card and an HDMI cable that connects to your TV. Experience once again one of the best games from the original PlayStation that changed gaming forever.');


INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 1, 'https://photos.alexfreyr.com/game-covers/donkey-kong-cover.png', 'Donkey Kong 64 from Nintendo');
INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 2, 'https://photos.alexfreyr.com/game-covers/legend-of-zelda-linktothepast-cover.jpg', 'The Legend of Zelda - Super Nintendo');
INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 3, 'https://photos.alexfreyr.com/game-covers/super-mario-64-cover.jpg', 'Super Mario, Nintendo 64');
INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 4, 'https://photos.alexfreyr.com/game-covers/shadow_of_the_beast_3_amiga.jpg', 'The Shadow of the Beasr - 512k required!!1');
INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 5, 'https://photos.alexfreyr.com/game-covers/sonic_the_hedgehog_2.jpg', 'Sonic the Hedgehof II - Best from SEGA');
INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 6, 'https://photos.alexfreyr.com/game-covers/Turrican.jpg', 'Turrican');

INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 7, 'https://photos.alexfreyr.com/game-covers/super_nes_classic.jpg', 'The best retro console you can buy');
INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 8, 'https://photos.alexfreyr.com/game-covers/sega_genesis.jpg', 'The best option for SEGA fans');
INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 9, 'https://photos.alexfreyr.com/game-covers/atari_flashback.jpg', 'The best option for SEGA fans');
INSERT INTO Store_ProductPhoto (product_id_id, path, alt) VALUES ( 10, 'https://photos.alexfreyr.com/game-covers/sony_playstatoin.jpg', 'The best retro console with 3D games');



INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (1, 1, 5, 'Stands tall over other similar-minded action titles.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (2, 1, 2, 'Nothing but pure 100% fun, challenging, and lengthy.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (3, 1, 5, 'It has quickly grown to become the standard by which almost all');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (4, 1, 1, ' ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (5, 1, 1, 'While Sega Ages: Sonic the Hedgehog 2 isnt the best version of');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (6, 1, 1, 'I first played Turrican on the C64 when I was about 10 and it');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (1, 2, 5, 'The best game I will ever play! The collectibles, the music.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (2, 2, 4, 'This game its amazing, since the start any gamer would see this.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (3, 2, 3, 'The distribution of power stars in the levels is horrendous.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (4, 2, 2, ' ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (5, 2, 1, 'It comes as little surprise but Sonic the Hedgehog 2 remains a.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (6, 2, 1, ' ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (1, 3, 4, 'The best 3d platform game along with super mario 64,excellent.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (2, 3, 4, 'An epic adventure that is among the best N64 games.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (3, 3, 4, 'THIS GAME AGED BAD nothing to add.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (4, 3, 3, ' ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (5, 3, 2, 'A brilliant presentation of a fantastic platformer, with a reasonable ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (6, 3, 1, ' ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (1, 4, 5, 'Those who obtain perverse pleasure from collecting every last coin and ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (2, 4, 2, ' ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (3, 4, 3, 'If you want to play the very best 3D platform game that has been made.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (4, 4, 1, ' ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (5, 4, 2, 'In spite of featuring less content than the titles 2013 remake for iOS.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (6, 4, 1, 'When I think of the time that I spent playing this game, very fond');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (1, 5, 5, 'Some gamers will feel overwhelmed just as I did on a few occasions.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (2, 5, 4, '10 / 10 / 10 / 10 - platinum [first ever perfect score]');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (3, 5, 2, 'Another true classic. This game was revolutionary and is a masterpiece.');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (4, 5, 2, ' ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (5, 5, 1, 'Sonic The Hedgehog 2 continues to be pure magic and no matter how many ');
INSERT INTO Store_Review (product_id_id, user_id_id, rating, comment) VALUES (6, 5, 2, 'Turrican is a game almost solely created by one guy. The fact it stand up to and in some regards best Metroid I/II is very impressive stuff.');



INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (1, 12.39, 'A0B43C01889D0119','2019-4-5', True);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (2, 9.00, 'AFB03C01889D0120','2019-4-2', True);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (3, 15.00, 'AFB40C01889D0121','2019-4-3', True);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (4, 21.90, 'AFB43C0089D0122','2019-3-29', True);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (5, 17.79, 'AFB43C01009D0123','2019-4-7', True);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (3, 55.39, 'AFB43C00889D0119','2020-4-5', True);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (4, 35.55, 'AFB00C01889D0120','2020-4-2', True);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (5, 25.00, 'AFB43C01889D0121','2020-4-3', True);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (1, 15.90, 'AFB43C01889D0122','2020-3-29', False);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (2, 45.79, 'AFB43C01889D0123','2020-4-7', False);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (3, 25.00, 'AFB43C01889D0121','2020-4-3', False);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (4, 15.90, 'AFB43C01889D0122','2020-3-29', False);
INSERT INTO checkout_order (user_id_id, total_price, tracking_nr, date, confirmed) VALUES (5, 45.79, 'AFB43C01889D0123','2020-4-7', False);


INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (1, 1, 3, 12.25, 1);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (2, 3, 3, 68.43, 2);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (3, 5, 1, 9.89, 3);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (4, 7, 1, 12.99, 4);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (5, 5, 3, 33.33, 5);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (5, 9, 1, 12.25, 5);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (5, 6, 1, 68.43, 5);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (3, 4, 1, 9.89, 6);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (4, 2, 3, 12.99, 7);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (5, 1, 1, 33.33, 8);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (1, 4, 1, 12.25, 9);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (2, 6, 3, 68.43, 10);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (3, 7, 1, 9.89, 11);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (4, 5, 1, 12.99, 12);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (5, 2, 3, 33.33, 13);
INSERT INTO checkout_orderproduct (user_id_id, product_id_id, quantity, price, order_id_id) VALUES (1, 2, 1, 12.25, 1);

INSERT INTO home_news (title, date, short, article) VALUES ('New Super Mario Bros. speedrun record!', '2020-04-04',
    'A new speedrun record was set in the game Super Mario Bros.! Until now, the world record was a time of 4 minutes, 55 seconds, and 583 milliseconds.',
    '<p>A new speedrun record was set in the game Super Mario Bros.! Until now, the world record was a time of 4 minutes, 55 seconds, and 583 milliseconds. The runner tonyterrific broke that record with a time of 4 minutes, 55 seconds, and 427 milliseconds!</p><p>He said he was really surprised when he realized he had broken the record, as his only focus was going as fast as he could to try to break his own previous record, and not expecting to break the world record. His previous record was a time of 4 minutes, 57 seconds, and 237 milliseconds. So he went from 21st place to 1st place, and now holds a world record!</p>');
INSERT INTO home_news (title, date, short, article) VALUES ('New PlayStation releases coming soon',  '2020-04-04',
    'It has been reported that PlayStation will be releasing a good deal of new games for the second half of this year and early next year.',
    '<p>It has been reported that PlayStation will be releasing a good deal of new games for the second half of this year and early next year.</p><p>Both games, and of course, the highly anticipated PlayStation 5 will make an appearance soon. The games that are expected, will be for both PS4 and PS5. These upcoming releases are sure to appeal to people‘s versatile tastes, as the the genres of the games are versatile. For instance, you can expect action, adventure, strategy and sports games. We can‘t tell you the names of the games just yet, but just know that you‘re in for a great game season!</p>');
INSERT INTO home_news (title, date, short, article) VALUES ('Pilots Of Darsalon - Upcoming PC game',  '2020-05-14',
    'On the 28th of May, Dr. Kucho Games will be releasing their graphically appealing Thrust inspiration on Steam, which they are calling ‘Pilots of Darsalon‘.',
    '<p>I‘m sure many retro gamers will remember Thrust, which was first published by Firebird Software Ltd and released in 1986. It also originally came on a multitude of systems including the Atari 2600, Amstrad CPC, Atari 8-bit, Atari ST, BBC Micro, Commodore 16, Plus/4, Commodore 64, Electron, Vectrex, and ZX Spectrum. Well if you wait until the 28th of May on Steam, Dr. Kucho Games will be releasing their graphically appealing Thrust inspiration, which they are calling ‘Pilots of Darsalon‘.</p><p>According to the creators this is a physics based arcade game, inspired by the very early classics such as "Thrust" , "Gravitar", "Lunar lander" and "Solar Jetman" but with a strong Commodore 64 feel added to the game as well. As for features which sound rather cool, Pilots of Darsalon will feature physics based control, an online world leader board, CRT filters, a C64(ish) color palette, unique pixel art blending dynamic lighting 2D and 3D graphics, 8bit music based on the C64‘s SID chip, 15 stages of difficulty and much much more!</p>');

