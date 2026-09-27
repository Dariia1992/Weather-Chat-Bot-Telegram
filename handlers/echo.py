from aiogram import Router, types


router = Router()


@router.message()
async def echo_message(message: types.Message):
    await message.answer("Incorrect input, please try again.")