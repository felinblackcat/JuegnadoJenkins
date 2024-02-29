node {
    stage("BuildTesting") {
        sh "pytest --cov=. --cov-fail-under=90"
    }
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