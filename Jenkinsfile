pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/1992ron/End-to-End-Testing-Framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Web Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'pytest test_cases/web_tests/ --alluredir=allure-results'
                }
            }
        }

        stage('API Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'pytest test_cases/api_tests/ --alluredir=allure-results'
                }
            }
        }

        stage('Database Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'pytest test_cases/db_tests/ --alluredir=allure-results'
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
                        pytest test_cases\\desktop_app_tests\\ --alluredir=allure-results

                        REM Kill WinAppDriver after tests
                        taskkill /IM WinAppDriver.exe /F || exit 0
                    '''
                }
            }
        }

        stage('Mobile Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                        REM Run Appium server
                        start /B appium

                        REM Run mobile tests
                        pytest test_cases\\mobile_tests\\ --alluredir=allure-results

                        REM Kill Appium server
                        taskkill /IM node.exe /F || exit 0
                    '''
                }
            }
        }

        stage('Electron Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '''
                        REM Start Todolist Electron app
                        start "" "C:\\Full Stack Automation Project\\Todolist-Setup.exe"

                        REM Run electron tests
                        pytest test_cases\\electron_app_tests\\ --alluredir=allure-results

                        REM Kill Todolist app after tests
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
