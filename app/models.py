from django.db import models

# Create your models here.
# Django ORM
class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    initial_price = models.FloatField(verbose_name='Preço inicial')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'


class MyTeam(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    players = models.ManyToManyField(Player, verbose_name='Jogadores')
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Meu Time'
        verbose_name_plural = 'Meus Times'


class Match(models.Model):
    match_date = models.DateTimeField(verbose_name='Data/Hora do jogo')
    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_a_matches', verbose_name='Time A')
    team_b = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_b_matches', verbose_name='Time B')
    team_a_goals = models.IntegerField(default=0, verbose_name='Gols do Time A')
    team_b_goals = models.IntegerField(default=0, verbose_name='Gols do Time B')

    def __str__(self) -> str:
        return f'{self.team_a} vs {self.team_b}'
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

class Action(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT, verbose_name='Jogador')
    team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name='Time')
    minutes = models.IntegerField(verbose_name='Minutos')
    match = models.ForeignKey(Match, on_delete=models.PROTECT, verbose_name='Jogo')

    class Actions(models.TextChoices):
        GOAL = 'goal', 'Gol'
        ASSIST = 'assist', 'Assistência'
        YELLOW_CARD = 'yellow card', 'Cartão Amarelo'
        RED_CARD = 'red card', 'Cartão Vermelho'
    
    action = models.CharField(max_length=50, choices=Actions.choices, verbose_name='Ação')

    def __str__(self) -> str:
        return f'{self.player} - {self.action}'
    
    class Meta:
        verbose_name = 'Ação do Jogo'
        verbose_name_plural = 'Ações do Jogo'