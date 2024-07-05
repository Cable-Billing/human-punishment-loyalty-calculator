![image](https://cf.geekdo-images.com/3vOdrN4dDxNP7gjZgoWGdQ__opengraph/img/rFcAZ6ihwNWnalSo-o4wwLty-lU=/0x0:4500x2363/fit-in/1200x630/filters:strip_icc()/pic3662950.jpg)

# Loyalty Calculator

This was created for the game Human Punishment.
Some friends have a hard time working out their loyalty in the game so this was a project to create a mobile web app to help them.

[Human Punishment: Social Deduction 2.0 Rulebook](https://cdn.1j1ju.com/medias/68/0b/3c-human-punishment-social-deduction-2-0-rulebook.pdf)

It also doubles as me learning Docker.

# Development Software Requirements

- Docker (that is pretty much it, unless you want to run the individual parts separately, but it isn't designed for that)

# How to Run

In the project there is a `Compose-Deployment` run configuration for those who use JetBrains IDEs. However, you can always run the command manually.

```bash
docker compose -f compose.yml -p human-punishment-loyalty-calculator up --always-recreate-deps --remove-orphans -d --build
```

# Database Migrations

The database migration files are to be stored in `./db/migrations/` and need to be in the format of `yyyyMMddHHmm.sql`.