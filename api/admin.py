from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Imovel, Contrato, Pagamento

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Dados do sistema de aluguéis",
            {
                "fields": (
                    "celular",
                    "tipo",
                )
            }
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Dados do sistema de aluguéis",
            {
                "fields": (
                    "email",
                    "celular",
                    "tipo",
                )
            }
        ),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "tipo",
        "is_staff",
        "is_active",
        "celular"
    )

    list_filter = (
        "tipo",
        "is_staff",
        "is_active",
    )

admin.site.register(Imovel)
admin.site.register(Contrato)
admin.site.register(Pagamento)
