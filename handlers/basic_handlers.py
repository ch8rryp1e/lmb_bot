from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder
router = Router()

TEXT_QUESTIONS = [
    "Отмечаете ли Вы снижение общего уровня энергии, ощущение, что сил стало меньше?",
    "Отмечаете ли Вы перепады настроения, плаксивость, тревожность, апатию?",
    "Сколько из этих проблем с весом Вы можете отнести к себе?\n 1. Стала набирать вес, хотя в питании и физической нагрузке ничего не менялось.\n 2. Лишний вес образовался именно вокруг живота.\n 3. Стало сложнее удерживать здоровый вес.",
    "Сколько из этих проблем интимной жизни вы стали замечать (ранее не было)?\n 1. Нет желания.\n 2. Сухость и боль во время полового акта.\n 3. Притупление чувствительности эрогенных зон.\n 4. Проблемы с достижением оргазма.",
    "Сколько их этих проблем Вы можете отнести к себе?\n 1. Недержание мочи при смехе, чихании, стрессе, кашле.\n 2. Внезапные позывы в туалет.\n 3. Неспособность терпеть.\n 4. Ночные пробуждения в туалет?",
    "Сколько их этих гинекологических проблем у Вас присутствуют?\n 1. Зуд, жжение, раздражение во влагалище\n 2. Частые циститы, вагиниты, вагинозы, молочницы",
    "Сколько из этих изменений в менструальном цикле Вы заметили?\n 1. Менструации пропадают на пару месяцев, потом возобновляются.\n 2. Цикл стал короче/длиннее.\n 3. Количество дней менструации сократилось до 2-4.\n 4. Кровотечения стали более обильными или, наоборот, скудными.\n 5. Менструации стали более болезненными.",
]

PHOTO_Q1 = "AgACAgIAAxkBAAM1aaM573XQzzKiNWk3rAn4BaBcxqwAAgQUaxtYpSFJXkga2AhqfnMBAAMCAAN5AAM6BA"
PHOTO_Q2 = "AgACAgIAAxkBAANBaaNH2Hr1Xh2OBDXHKNyOGkbW8usAAk4UaxtYpSFJ_8mvKf2cGugBAAMCAAN5AAM6BA"
PHOTO_Q3 = "AgACAgIAAxkBAANMaaNJ36J6glsDQ7_hdbw8gtSpH_AAAl4UaxtYpSFJFaRAIDOtavABAAMCAAN5AAM6BA"
PHOTO_Q4 = "AgACAgIAAxkBAANOaaNKwupTwwwMYzfkzRvd4xEsZ5AAAoIUaxtYpSFJZ9LEC0MWwa8BAAMCAAN5AAM6BA"


PHOTO_SCORES = {
    "none": 0,
    "one": 1,
    "several": 3,
    "all": 5,
}
TEXT_SCORES = {
    "no": 0,
    "partly": 1,
    "yes": 3,
}

#  4*5 + 7*3 = 20 + 21 = 41

def get_result(score: int) -> str:
    if score <= 13:
        return (
            " <b>Lorem ipsum</b>\n\n"
            "ojigtfvghjioplkji "
            "Ваш результат: <b>{score} из 41</b>"
        )
    elif score <= 27:
        return (
            " <b>lorem ipsum dolor</b>\n\n"
            "tf7ft7ygt76itg8"
            "Ваш результат: <b>{score} из 41</b>"
        )
    else:
        return (
            " <b>Lorem ipsum dolor sit amet</b>\n\n"
            "Нtrfgp0987yhj "
            "Ваш результат: <b>{score} из 41</b>"
        )



class TestState(StatesGroup):
    running = State()


def photo_keyboard(q_num: int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Ничего из этого", callback_data=f"pq{q_num}_none")
    builder.button(text="Одно",            callback_data=f"pq{q_num}_one")
    builder.button(text="Несколько",       callback_data=f"pq{q_num}_several")
    builder.button(text="Все это есть",    callback_data=f"pq{q_num}_all")
    builder.adjust(2)
    return builder.as_markup()


def text_keyboard(q_num: int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Нет",        callback_data=f"tq{q_num}_no")
    builder.button(text="Отчасти да", callback_data=f"tq{q_num}_partly")
    builder.button(text="Точно да",   callback_data=f"tq{q_num}_yes")
    builder.adjust(3)
    return builder.as_markup()




@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Здравствуйте!\n\n"
        "В этом тесте собраны признаки, "
        "по которым мы с коллегами можем увидеть "
        "дефицит половых гормонов у женщины.\n"
        "Речь идёт о:\n"
        "• эстрогенах\n"
        "• тестостероне\n"
        "• прогестероне\n"
        "Даже без погружения в результаты анализов."
    )

    builder = InlineKeyboardBuilder()
    builder.button(text="Давайте начнём ", callback_data="start_test")
    await message.answer(
        "Благодаря тестированию Вы сможете понять:\n\n"
        "1. Насколько полон Ваш гормональный ресурс, чтобы Вы оставались энергичной и красивой долгие годы.\n"
        "2. Есть ли предвестники приближения менопаузы.\n"
        "3. Что можно сделать прямо сейчас, не дожидаясь похода к врачу.",
        reply_markup=builder.as_markup()
    )


PHOTO_FILES = {1: PHOTO_Q1, 2: PHOTO_Q2, 3: PHOTO_Q3, 4: PHOTO_Q4}
PHOTO_CAPTIONS = {
    1: "Сколько из этих состояний Вы отмечаете у себя часто?",
    2: "Сколько из этих состояний Вы отмечаете у себя часто?",
    3: "ТСколько из этих состояний Вы отмечаете у себя часто?",
    4: "Сколько из этих состояний Вы отмечаете у себя часто?",
}

@router.callback_query(F.data == "start_test")
async def question_photo_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(TestState.running)
    await state.update_data(score=0)
    await callback.message.answer_photo(
        photo=PHOTO_FILES[1],
        caption=PHOTO_CAPTIONS[1],
        reply_markup=photo_keyboard(1)
    )


ALL_PHOTO_CALLBACKS = {f"pq{i}_{a}" for i in range(1, 5) for a in PHOTO_SCORES}

@router.callback_query(F.data.in_(ALL_PHOTO_CALLBACKS), TestState.running)
async def handle_photo_question(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    parts = callback.data.split("_")   
    q_num = int(parts[0][2:])        
    answer = parts[1]                

    data = await state.get_data()
    score = data.get("score", 0) + PHOTO_SCORES[answer]
    await state.update_data(score=score)

    if q_num < 4:
        await callback.message.answer_photo(
            photo=PHOTO_FILES[q_num + 1],
            caption=PHOTO_CAPTIONS[q_num + 1],
            reply_markup=photo_keyboard(q_num + 1)
        )
    else:
        await callback.message.answer(
            TEXT_QUESTIONS[0],
            reply_markup=text_keyboard(1)
        )



ALL_TEXT_CALLBACKS = {f"tq{i}_{a}" for i in range(1, 8) for a in TEXT_SCORES}

@router.callback_query(F.data.in_(ALL_TEXT_CALLBACKS), TestState.running)
async def handle_text_question(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    parts = callback.data.split("_")   
    q_num = int(parts[0][2:])          
    answer = parts[1]                  

    data = await state.get_data()
    score = data.get("score", 0) + TEXT_SCORES[answer]
    await state.update_data(score=score)

    if q_num < 7:
        await callback.message.answer(
            TEXT_QUESTIONS[q_num],     
            reply_markup=text_keyboard(q_num + 1)
        )
    else:
        
        await state.clear()
        result_template = get_result(score)
        result_text = result_template.replace("{score}", str(score))
        await callback.message.answer(result_text, parse_mode="HTML")

# @router.message(F.photo)
# async def get_file_id(message: types.Message):
#     file_id = message.photo[-1].file_id
#     await message.answer(f"Ваш file_id:\n<code>{file_id}</code>", parse_mode="HTML")
