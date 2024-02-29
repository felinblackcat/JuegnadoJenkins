node {
    def commited_email = sh(script: "git rev-parse HEAD",  returnStdout: true).trim()
    def commited_hash = sh(script: "git log -1 --format='%ae'",  returnStdout: true).trim()
    def coverage
    echo commited_email
    echo commited_hash
    stage("BuildTesting") {
        def customImage = docker.build("juegnadojenkins:latest")
        coverage = sh(script: "docker run juegnadojenkins pytest --junitxml=./test.xml --cov=. --cov-fail-under=90 | grep TOTAL| awk '{print \$4}' | tr -d %", returnStdout: true).trim()
        sh "ls"
        sh 'ls app'
    }
    echo coverage
    stage("CheckStaticCode") {
        echo "Hello, CheckStaticCode!"

    }
    stage("RunUnitaryTest") {
        echo "Hello, RunUnitaryTest!"
     }
    stage("BuildPreprod") {
        echo "Hello, BuildPreprod!"
    }
    stage("IntegrationTest") {
        echo "Hello, IntegrationTest!"
    }
    stage("CheckCVE") {
        echo "Hello, CheckCVE!"
    }
    stage("SendRegistry") {
        echo "Hello, SendRegistry!"

    }
    stage("UATDeploy") {
        echo "Hello, UAT Deploy!"
    }
    
}