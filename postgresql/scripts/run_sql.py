import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SQL_DIR = PROJECT_ROOT / "sql"


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"Variável de ambiente ausente: {name}")

    return value


def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    postgres_host = get_required_env("POSTGRES_HOST")
    postgres_port = get_required_env("POSTGRES_PORT")
    postgres_db = get_required_env("POSTGRES_DB")
    postgres_user = get_required_env("POSTGRES_USER")
    postgres_password = get_required_env("POSTGRES_PASSWORD")

    sql_files = sorted(SQL_DIR.glob("*.sql"))

    if not sql_files:
        print(f"Nenhum arquivo .sql encontrado em: {SQL_DIR}")
        return

    print(f"Banco: {postgres_db}")
    print(f"Usuário: {postgres_user}")
    print(f"Arquivos encontrados: {len(sql_files)}")
    print("-" * 80)

    env = os.environ.copy()
    env["PGPASSWORD"] = postgres_password

    for sql_file in sql_files:
        print(f"Executando: {sql_file.name}")

        command = [
            "psql",
            "-h",
            postgres_host,
            "-p",
            postgres_port,
            "-U",
            postgres_user,
            "-d",
            postgres_db,
            "-v",
            "ON_ERROR_STOP=1",
            "-f",
            str(sql_file),
        ]

        result = subprocess.run(command, env=env)

        if result.returncode != 0:
            raise RuntimeError(f"Erro ao executar o arquivo: {sql_file.name}")

        print(f"OK: {sql_file.name}")
        print("-" * 80)

    print("Todos os arquivos SQL foram executados com sucesso.")


if __name__ == "__main__":
    main()