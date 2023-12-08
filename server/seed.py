#!/usr/bin/env python3

# Standard library imports
from random import choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Stream, Anime, Platform

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database

    print('Deleting data...')
    Stream.query.delete()
    Anime.query.delete()
    Platform.query.delete()

    print('Creating streams...')

    s1 = Stream(name='Crunchyroll', image='https://image.roku.com/developer_channels/prod/413146628c55392af8378cf9e9885bcacbe9ae4509647db88dbfaf0017e86739.png')

    s2 = Stream(name='Hulu', image='https://reviewed-com-res.cloudinary.com/image/fetch/s--xT7E_lQY--/b_white,c_fill,cs_srgb,f_auto,fl_progressive.strip_profile,g_auto,h_972,q_auto,w_972/https://reviewed-production.s3.amazonaws.com/1591287416567/Hulu_Logo.jpg')

    s3 = Stream(name='Netflix', image='https://static-00.iconduck.com/assets.00/netflix-icon-icon-2048x2048-yj41gpvr.png')

    streams = [s1, s2, s3]

    print('Creating animes...')

    #Crunchyroll
    a1 = Anime(name='Dr. Stone', image='https://i1.sndcdn.com/artworks-000663819439-5ptp75-t500x500.jpg', num_episodes=57, summary="After several millennia, high schooler Taiju awakens and finds himself lost in a world of statues. However, he's not alone. His science-loving friend Senku's been up and running for a few months and he's got a grand plan in mind, to kickstart civilization with the power of science.", completed='False', likes=502)

    a2 = Anime(name='Attack on Titan', image='https://i1.sndcdn.com/artworks-000123690573-uhuyr7-t500x500.jpg', num_episodes=99, summary="It is set in a world where humanity is forced to live in cities surrounded by three enormous walls that protect them from gigantic man-eating humanoids referred to as Titans; the story follows Eren Yeager, who vows to exterminate the Titans after they bring about the destruction of his hometown and the death of his mother. ", completed='True', likes=873)

    a3 = Anime(name='Plunder', image='https://static.wikia.nocookie.net/jpop/images/d/dc/Plunderer_regulaar.jpg/revision/latest?cb=20200111173709', num_episodes=24, summary="In a post-apocalyptic world, each citizen has their identity branded with their own 'Count,' which defines their livelihood. But a mysterious figure has an agenda to steal away these Counts.", completed='False', likes=133)

    a4 = Anime(name='Jujutsu Kaisen', image='https://i1.sndcdn.com/artworks-88C70vpKYuxK7vjI-BlMDrA-t500x500.jpg', num_episodes=44, summary="Follows the story of Yuji Itadori, an ordinary boy who crosses paths with Megumi Fushiguro, a Jujutsu Sorcerer searching for a powerful Cursed Object known as Ryomen Sukuna's finger. Unintentionally, Yuji's friends unseal the Cursed Object, attracting dangerous Curses to their location.", completed='False', likes=1053)

    a5 = Anime(name='My Hero Academia', image='https://m.media-amazon.com/images/I/61XiBl+CLQL._UXNaN_FMjpg_QL85_.jpg', num_episodes=144, summary="Academies across the globe train their students to learn to fight crime with their powers. Izuku Midoriya, a boy born without any powers, dreams of being able to become a super hero too, but gets bullied for his unrealistic dreams.", completed='False', likes=1206)

    a6 = Anime(name="The Saint's Magic is Omnipotent", image='https://i1.sndcdn.com/artworks-LzExW1UQaa8Qsipf-XRf6ew-t500x500.jpg', num_episodes=22, summary="Sei Takanashi, an office worker, is returning home late at night but is summoned to the magic world of Salutania; the summoning, however, is a one way kidnapping with no way to send her home. Unfazed, Sei follows her own devices and sets her sights on being a researcher at the Medicinal Flora Research Institute, an establishment known for its studies regarding herbs and potions. While indulging in her latest passion, Sei has a fateful encounter with the commander of the Third Order of Knights. But little does she know, her aptitude as a Saint will continue to exert its influence over her new life.", completed='False', likes=75)

    #Hulu
    a7 = Anime(name='Bleach', image='https://m.media-amazon.com/images/I/51JGVIPwznL.jpg', num_episodes=392, summary="The story follows the adventures of Ichigo Kurosaki after he obtains the powers of a Soul Reaper—a death personification similar to the Grim Reaper—from another Soul Reaper, Rukia Kuchiki.", completed='False', likes=4058)

    a8 = Anime(name='Demon Slayer', image='https://i1.sndcdn.com/artworks-d0P76G4ZOZHLx94d-JKcXtg-t500x500.jpg', num_episodes=55, summary="A family is attacked by demons and only two members survive - Tanjiro and his sister Nezuko, who is turning into a demon slowly. Tanjiro sets out to become a demon slayer to avenge his family and cure his sister.", completed='False', likes=2861)

    a9 = Anime(name='The Rising of Shield Hero', image='https://honeysanime.com/wp-content/uploads/2021/07/shield-hero-season-2-kv2-500x500.jpeg', num_episodes=47, summary="Follows the story of Naofumi Iwatani a Japanese college student summoned to a fantasy world to become one of four heroic saviors. The four heroes must fight against the waves of calamity, portals that open in the sky and pour monsters into the world.", completed='False', likes=146)

    a10 = Anime(name='That Time I Was Reincarnated as a Slime', image='https://witchesandrayguns.files.wordpress.com/2019/08/slime.jpg?w=500', num_episodes=60, summary="Satoru Mikami, a salaryman who is murdered and then reincarnated in a sword and sorcery world as a titular slime, who goes on to gather allies to build his own nation of monsters.", completed='False', likes=179)

    a11 = Anime(name='Mushoku Tensei Jobless Reincarnation', image='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/1f825950-38b7-4fa6-a3fb-5d865abebe6c/dex05dd-bd5fb094-3eb4-4f3c-a0db-f5c81b15217e.png/v1/fill/w_500,h_500/mushoku_tensei_isekai_ittara_honki_dasu_part2_icon_by_milanroberto9_dex05dd-fullview.png', num_episodes=37, summary="It follows jobless and hopeless man who dies after having a sad and reclusive life and reincarnates in a fantasy world while keeping his memories, determined to enjoy his new life without regrets under the name Rudeus Greyrat.", completed='False', likes=87)

    a12 = Anime(name='Tokyo Ghoul', image='https://external-preview.redd.it/IcnRgP6Uq_AToRAz3Mq-WbXQjORT495C4KCpuFg64yI.jpg?auto=webp&s=d125c991455cbd3db69ed3dd37a2e530f0a07048', num_episodes=96, summary="A college student is attacked by a ghoul, a being that feeds on human flesh. He later receives an organ transplant from the ghoul, becoming part monster himself.", completed='True', likes=64)

    #Netflix
    a13 = Anime(name='Black Clover', image='https://i0.wp.com/nerdalertnews.net/wp-content/uploads/2023/01/ENUS_BlackClover_Main_Vertical_RGB_PRE-1.jpg?resize=500%2C500&ssl=1', num_episodes=171, summary="Set in a world where everyone is given the ability to use magic, the story follows Asta, a young boy born without any magic power who is given a rare grimoire that grants him anti-magic abilities. With his fellow mages from the Black Bulls, Asta plans to become the next Wizard King.", completed='False', likes=173)

    a14 = Anime(name='Inuyasha', image='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2a07ecf5-7903-4d25-8b86-c76727256329/d3ft33o-494b6a91-609a-4bb6-ac44-ed37b257fdea.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJhMDdlY2Y1LTc5MDMtNGQyNS04Yjg2LWM3NjcyNzI1NjMyOVwvZDNmdDMzby00OTRiNmE5MS02MDlhLTRiYjYtYWM0NC1lZDM3YjI1N2ZkZWEuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.uIa-XZe9tDKeIN1aGY6xHvn0mP4UJHEMsProPk8HMnw', num_episodes=193, summary="A Kagome, teenage girl periodically, travels back in time to feudal Japan to help Inuyasha, a young half-demon, recover the shards of a jewel of great power. Through their quest they are joined by the lecherous monk Miroku, the demon slayer Sango, and the fox demon Shippō. Together, they journey to restore the Shikon Jewel before it falls into the hands of the evil half-demon Naraku.", completed='True', likes=8037)

    a15 = Anime(name='One Piece', image='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/03444932-1ae8-44f5-8035-dbde879dcb75/d7e2l5l-e6914afa-25f9-4a97-ad7c-7baca7804aff.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzAzNDQ0OTMyLTFhZTgtNDRmNS04MDM1LWRiZGU4NzlkY2I3NVwvZDdlMmw1bC1lNjkxNGFmYS0yNWY5LTRhOTctYWQ3Yy03YmFjYTc4MDRhZmYuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.7O7gC_d7GOgxbwfUPSQkna859GB98PL10fO98Qy0KUc', num_episodes=1087, summary="Luffy is a young adventurer who has longed for a life of freedom ever since he can remember. He sets off from his small village on a perilous journey to find the legendary fabled treasure, ONE PIECE, to become King of the Pirates!", completed='False', likes=9542)

    a16 = Anime(name='Records of Ragnarok', image='https://static.wikia.nocookie.net/shuumatsu-no-valkyrie/images/9/91/Fukahi.png/revision/latest?cb=20230713174705', num_episodes=27, summary="RECORD OF RAGNAROK is an action anime about humans and gods fighting in arena combat. A convention of gods must decide to let humanity survive or perish. Ultimately, they choose to test humanity by facing off against them in a series of thirteen showdowns called Ragnarok.", completed='False', likes=359)

    a17 = Anime(name='Avatar the Last Airbender', image='https://i1.sndcdn.com/artworks-3Zj1tR9oy79Yx7j4-7TyDCA-t500x500.jpg', num_episodes=62, summary="Centered around the journey of twelve-year-old Aang, the current Avatar and last survivor of his nation, the Air Nomads, along with his friends Katara, Sokka, and later Toph, as they strive to end the Fire Nation's war against the other nations of the world.", completed='True', likes=6874)

    a18 = Anime(name='Sword Art Online', image='https://www.onrpg.com/wp-content/uploads/2014/08/Mabinogi_SAO.jpg', num_episodes=100, summary="The story of a multiplayer virtual-reality game that takes a deadly turn when players discover they can't escape of their own will but must play to victory or to death.", completed='False', likes=471)

    animes = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18]

    print('Creating platforms...')
    p1 = Platform(anime=a1, stream=s1)
    p2 = Platform(anime=a2, stream=s1)
    p3 = Platform(anime=a3, stream=s1)
    p4 = Platform(anime=a4, stream=s1)
    p5 = Platform(anime=a5, stream=s1)
    p6 = Platform(anime=a6, stream=s1)
    p7 = Platform(anime=a7, stream=s2)
    p8 = Platform(anime=a8, stream=s2)
    p9 = Platform(anime=a9, stream=s2)
    p10 = Platform(anime=a10, stream=s2)
    p11 = Platform(anime=a11, stream=s2)
    p12 = Platform(anime=a12, stream=s2)
    p13 = Platform(anime=a13, stream=s3)
    p14 = Platform(anime=a14, stream=s3)
    p15 = Platform(anime=a15, stream=s3)
    p16 = Platform(anime=a16, stream=s3)
    p17 = Platform(anime=a17, stream=s3)
    p18 = Platform(anime=a18, stream=s3)
    p19 =Platform(anime=a1, stream = s3)

    platforms = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19]

    db.session.add_all(streams)
    db.session.add_all(animes)
    db.session.add_all(platforms)
    db.session.commit()

    print('Seeding done!')

