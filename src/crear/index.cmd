@echo off
doskey crear_commit=python "%~dp0crear_commit.py" $1 $2
doskey crear_repo=python "%~dp0crear_repo.py" $1 $2