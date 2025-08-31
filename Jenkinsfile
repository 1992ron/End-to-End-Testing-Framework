pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Web Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                        call venv\\Scripts\\activate.bat
                        pytest test_cases/web_tests/ --alluredir=allure-results
                    '''
                }
            }
        }

        stage('API Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                        call venv\\Scripts\\activate.bat
                        pytest test_cases/api_tests/ --alluredir=allure-results
                    '''
                }
            }
        }

        stage('Database Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                        call venv\\Scripts\\activate.bat
                        pytest test_cases/db_tests/ --alluredir=allure-results
                    '''
                }
            }
        }

        stage('Desktop Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                        REM Start WinAppDriver
                        start "" "C:\\Program Files (x86)\\Windows Application Driver\\WinAppDriver.exe"

                        REM Run desktop tests
                        call venv\\Scripts\\activate.bat
                        pytest test_cases/desktop_tests/ --alluredir=allure-results

                        REM Kill WinAppDriver after tests
                        taskkill /IM WinAppDriver.exe /F
                    '''
                }
            }
        }

        stage('Electron Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                        REM Start TodoList Electron app
                        cd /d "C:\\Full Stack Automation Project"
                        start "" "Todolist-Setup.exe"

                        REM Run electron tests
                        call venv\\Scripts\\activate.bat
                        pytest test_cases/electron_app_tests/ --alluredir=allure-results

                        REM Kill TodoList app after tests
                        taskkill /IM Todolist.exe /F || exit 0
                    '''
                }
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
