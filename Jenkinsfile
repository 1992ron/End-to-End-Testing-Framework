pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/1992ron/End-to-End-Testing-Framework.git'
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
                    bat 'pytest test_cases/web_tests/ --alluredir=allure-results/web'
                }
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [
                    [path: 'allure-results/web']
                ]
            }
        }
    }
}
