from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Ticket(SQLModel, table=True):
    """
    Модель обращения в техподдержку.
    Соответствует требованиям Кейса ENIGMA (пункт 1: Структура веб-таблицы).
    """
    __tablename__ = "tickets"

    # --- Основные поля (Первичный ключ и даты) ---
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Дата поступления письма"
    )
    updated_at: Optional[datetime] = Field(default=None)

    # --- Данные из письма (Извлекает AI/Парсер) ---
    fio: Optional[str] = Field(default=None, description="Фамилия, имя, отчество отправителя")
    object_name: Optional[str] = Field(default=None, description="Название предприятия или объекта")
    phone: Optional[str] = Field(default=None, description="Контактный номер телефона")
    email: str = Field(..., description="Адрес электронной почты отправителя")

    # --- Данные о приборе ---
    device_serial: Optional[str] = Field(default=None, description="Заводской номер прибора (газоанализатора)")
    device_type: Optional[str] = Field(default=None, description="Модель или тип устройства")

    # --- Анализ AI (NLP) ---
    sentiment: Optional[str] = Field(
        default="neutral",
        description="Эмоциональный окрас (pos/neg/neu)"
    )
    issue_description: Optional[str] = Field(default=None,
                                             description="Краткое описание проблемы или запроса (Суть вопроса)")
    category: Optional[str] = Field(
        default=None,
        description="Категория запроса (неисправность/калибровка/документация)"
    )

    # --- Работа оператора и ответы ---
    status: str = Field(
        default="new",
        description="Статус обработки: new, processing, resolved"
    )
    ai_response_draft: Optional[str] = Field(
        default=None,
        description="Черновик ответа, сгенерированный AI на основе Базы Знаний"
    )
    final_response: Optional[str] = Field(
        default=None,
        description="Финальный текст ответа, отправленный клиенту"
    )
    is_sent: bool = Field(default=False, description="Флаг отправки ответа клиенту")