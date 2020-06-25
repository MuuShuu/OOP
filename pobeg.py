from sys import exit
from textwrap import dedent


class Scene:

    @staticmethod
    def enter():
        print('Технические неполадки.')
        exit(1)


class Engine:

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death:

    @staticmethod
    def enter():
        print("Печально")
        exit(1)


class House:

    @staticmethod
    def enter():
        print(dedent("""
            ...Вы очнулись. Смотря вокруг вы видите неразборчивый хаос.
            Все то ли бегут, то ли дерутся. Пытаясь сфокусироваться Вы видите как на Вас
            бежит человек. Возле себя вы видите ломик и пистолет. Что Вы вибирете?
            1.Ломик
            2.Пистолет
            """))

        action = input("> ")

        if action == "1":
            print(dedent("""
                Схватив ломик вы пытатесь ударить человека который
                на Вас бежит. Попав ему по плечу, человек умудряется Вас укусить.
                Смотря на человека Вы понимате что это зомби...
                """))
            return 'death'

        elif action == "2":
            print(dedent("""
                Схватив пистолет, Вы стараетесь прицелиться и производите 
                выстрел, попадая человеку в голову. Подойдя к телу Вы поимаете что это зомби
                Вспоминая как Вы тут очутились Вы вспоминате как по новостям рассказывали 
                за какой то вирус...
                """))
            return 'tunel'

        else:
            print("Выбирете цифру!")
            return 'house'


class Tunel:

    @staticmethod
    def enter():
        print(dedent("""
            ...стараясь вспомнить куда Вы напрявлялись, вспоминате что
            друг Вам рассказывал за готовящиеся к отлету ракеты, и что он будет Вас ждать
            на космодроме.
            Осмотревшись вокруг Вы видите несколько машин. В какую будем садиться?
            1.Кабриолет.
            2.Джип.
            3.Минивэн.
            """))

        action = input("> ")

        if action == "1":
            print(dedent("""
                Прыгнув в кабриолет, на давите газ в пол стараясь 
                как можно быстрей добраться до космодрома. Двигаясь на запредельной скорости
                Вы въезжаете в тунель. Как всегда бывает в таких случаях пропадает свет, 
                и Вы чувствуте что вы что то сбили, понимая что это было вы стараетесь выдавить 
                педаль максимально возможно, но увы, въезжая в толпу зомби которые разлетаются 
                как кегли, часть из них падают в Вашу машину, остреливаясь до последнего 
                патрона, Вас все равно кусают...
                """))
            return 'death'

        elif action == "2":
            print(dedent("""
                Забравшись в джип, Вы стараетесь завести этот кусок металла.
                Слыша как двигатель начал фыркать, Вы выжимаете газ в пол стараясь выжать
                из него все соки. По дороге Вам встречается тунель, заподозрив что то не ладное
                Вы еще сильней стараетесь нажать педаль, и не зря. Въехав в тунель вы видите 
                группу зомби, но Вам то что, Вы в джипе! Влетев на сумашедшей скорости 
                в эту толпу, такой она быть перестала. Проехав тунель вы въезжаете 
                на трассу ведущую на космодром.
                """))
            return 'kosmodrom'

        elif action == "3":
            print("Серьёзно!!? Минивэн!!?")
            return 'death'

        else:
            print("Выбирете чилсло!")
            return 'tunel'


class Kosmodrom:

    @staticmethod
    def enter():
        print(dedent("""
            Прибыв на космодром вы встречаете своего друга.
            Он говорит вам что есть четыре ракеты. Вы приходите ко мнению что их готовили
            заранее. Теперь вам нужно выбрать куда лететь.
            Выбирать нужно быстро!
            1.СССР.
            2.Пукан.
            3.Клайф.
            4.Кино.
            5.Огас.
            """))

        action = input("> ")

        if action == "1":
            print(dedent("""
                Вы направляетесь к ракете, попутно одевая и собирая то что нужно.
                Вы отправляетесь на планету СССР!
                """))
            return 'ussr'

        elif action == "2":
            print(dedent("""
                Вы направляетесь к ракете, попутно одевая и собирая то что нужно.
                Вы отправляетесь на планету Пукан!
                """))
            return 'pukan'

        elif action == "3":
            print(dedent("""
                Вы направляетесь к ракете, попутно одевая и собирая то что нужно.
                Вы отправляетесь на планету Клайф!
                """))
            return 'klaif'

        elif action == "4":
            print(dedent("""
                Вы направляетесь к ракете, попутно одевая и собирая то что нужно.
                Вы отправляетесь на планету Кино!
                """))
            return 'kino'

        elif action == "5":
            print(dedent("""
                Вы направляетесь к ракете, попутно одевая и собирая то что нужно.
                Вы отправляетесь на планету Огас!
                """))
            return 'ogas'


class USSR:

    @staticmethod
    def enter():
        print(dedent("""
            Вы прилетели на планету СССР.
            Но она уже развалилась.
            """))
        return 'death'


class Pukan:

    @staticmethod
    def enter():
        print(dedent("""
            Вы прилетели на планету Пукан.
            И сгорели.
            """))
        return 'death'


class Klaif:

    @staticmethod
    def enter():
        print(dedent("""
            Вы прилетели на планету Клайф.
            Что бы выжить нужно где-то жить или что-то есть. 
            Что будем делать первым?
            1.Построить ночлег.
            2.Засеить землю.
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                Вы построили дом, и легли спать.
                Вы так и не проснулись. Планета оказалась зыбучим песком.
                Все умерли.
                """))
            return 'death'

        elif choice == "2":
            print(dedent("""
                Вы засеили землю и легли спать.
                Вы так и не проснулись.
                Планета оказалась зыбучим песком.
                Все умерли.
                """))
            return 'death'

        else:
            print("Введите число!")
            return 'klaif'


class Kino:

    @staticmethod
    def enter():
        print(dedent("""
            Вы прилетели на планету Кино.
            На планете окозалось неизвестное Вам животное.
            В лапах Вы у него замечаете листок бумаги.Что попробуете сделать?
            1.Выдернуть листок.
            2.Осторожно разбудить.
            """))
        animal_move = False

        while True:
            choice = input("> ")

            if choice == "1":
                print("Зверь проснулся и откусил Вам голову.")
                return 'death'

            elif choice == "2" and not animal_move:
                print(dedent("""
                    Животное открывает свои глаза.Ваши дальнейшие действия?"
                    1.Забрать листок силой.
                    2.Попросить?
                    """))
                animal_move = True

            elif choice == "1" and animal_move:
                print("Зверь откусил Вам голову.")
                return 'death'

            elif choice == "2" and animal_move:
                return 'beseda'

            else:
                print("Выбирите какой то вариант.")
                return 'kino'


class Ogas:

    @staticmethod
    def enter():
        print(dedent("Что то происходит."))
        return 'death'


class Beseda:

    @staticmethod
    def enter():
        print("Зверь смотрит на Вас.\nИ спрашивает.\n- 'Каков смысл жизни?'")

        choice = input("> ")

        if choice == "42":
            print("Зверь отвечает Вам.\n- 'Добро пожаловать!'")
            exit(0)

        elif choice != "42":
            print("Зверь откусил Вам голову.")
            return 'death'

        else:
            print("Введите ответ.")


class TheEnd:

    @staticmethod
    def enter():
        print("Вы благополучно сбежали с планеты!")
        return 'finish'


class Map:
    
    scenes = {
        'house': House,
        'tunel': Tunel,
        'kosmodrom': Kosmodrom,
        'ussr': USSR,
        'pukan': Pukan,
        'klaif': Klaif,
        'kino': Kino,
        'death': Death,
        'finish': TheEnd,
        'beseda': Beseda,
        'ogas': Ogas,
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        kata = Map.scenes.get(scene_name)
        return kata

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('house')
a_game = Engine(a_map)
a_game.play()

# Коментарий для проверки