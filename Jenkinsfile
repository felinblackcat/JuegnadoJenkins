pipeline {
    agent any
    stages {
        stage("BuildTesting") {
            agent { dockerfile true }
            steps {
                echo "python --version"
            }
        }
        stage("CheckStaticCode") {
            steps {
                echo "Hello, CheckStaticCode!"
            }
        }
        stage("RunUnitaryTest") {
            steps {
                echo "Hello, RunUnitaryTest!"
            }
        }
        stage("BuildPreprod") {
            steps {
                echo "Hello, BuildPreprod!"
            }
        }
        stage("IntegrationTest") {
        steps {
            echo "Hello, IntegrationTest!"
        }
        }
        stage("CheckCVE") {
        steps {
            echo "Hello, CheckCVE!"
        }
        }
        stage("SendRegistry") {
        steps {
            echo "Hello, SendRegistry!"
        }
        }
        stage("UATDeploy") {
        steps {
            echo "Hello, UAT Deploy!"
        }
        }
    }
}