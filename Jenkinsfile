pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/02prem/IMT2020044_jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x func.py"
                sh "./func.py"
            }
        }
        stage('Test Code Passed') {
            steps {
                sh "chmod u+x unit_testcase_passed.py"
                sh "./unit_testcase_passed.py"
            }
        }
        stage('Test Code Failed') {
            steps {
                sh "chmod u+x unit_testcase_failed.py"
                sh "./unit_testcase_failed.py"
            }
        }
    } 
}