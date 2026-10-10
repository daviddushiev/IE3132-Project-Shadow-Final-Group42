
import socket
import subprocess
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


# T01 - Check rCTF platform
def check_rctf():
    try:
        with urlopen("http://127.0.0.1:8080/", timeout=5) as response:
            if response.status == 200:
                print("[PASS] T01 - rCTF platform is accessible")
                return True

        print("[FAIL] T01 - Unexpected HTTP response")
        return False

    except (HTTPError, URLError, TimeoutError) as error:
        print(f"[FAIL] T01 - {error}")
        return False


# T02 - Check PS-01 public website
def check_ps01():
    request = Request(
        "http://127.0.0.1:8082/",
        headers={"Host": "solace.test"}
    )

    try:
        with urlopen(request, timeout=5) as response:
            if response.status == 200:
                print("[PASS] T02 - PS-01 website is accessible")
                return True

        print("[FAIL] T02 - Unexpected HTTP response")
        return False

    except (HTTPError, URLError, TimeoutError) as error:
        print(f"[FAIL] T02 - {error}")
        return False


# T03 - Check PS-01 research archive
def check_research_archive():
    request = Request(
        "http://127.0.0.1:8082/",
        headers={"Host": "archive.solace.test"}
    )

    try:
        with urlopen(request, timeout=5) as response:
            if response.status == 200:
                print("[PASS] T03 - Research archive is accessible")
                return True

        print("[FAIL] T03 - Unexpected HTTP response")
        return False

    except (HTTPError, URLError, TimeoutError) as error:
        print(f"[FAIL] T03 - {error}")
        return False


# T04 - Check PS-02 research portal
def check_ps02():
    try:
        with urlopen("http://127.0.0.1:8081/", timeout=5) as response:
            if response.status == 200:
                print("[PASS] T04 - PS-02 research portal is accessible")
                return True

        print("[FAIL] T04 - Unexpected HTTP response")
        return False

    except (HTTPError, URLError, TimeoutError) as error:
        print(f"[FAIL] T04 - {error}")
        return False


# T05 - Check PS-01 DNS resolution
def check_dns():
    try:
        result = subprocess.run(
            [
                "dig",
                "@127.0.0.1",
                "-p", "1053",
                "archive.solace.test",
                "A",
                "+short"
            ],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        addresses = result.stdout.strip().splitlines()

        if "127.0.0.1" in addresses:
            print("[PASS] T05 - DNS resolves archive.solace.test")
            return True

        print(f"[FAIL] T05 - Unexpected DNS result: {addresses}")
        return False

    except (subprocess.SubprocessError, OSError) as error:
        print(f"[FAIL] T05 - DNS test error: {error}")
        return False


# T06 - Check PS-07 SSH connectivity
def check_ssh():
    try:
        with socket.create_connection(
            ("127.0.0.1", 2227),
            timeout=5
        ):
            print("[PASS] T06 - PS-07 SSH port 2227 is reachable")
            return True

    except OSError as error:
        print(f"[FAIL] T06 - SSH connection error: {error}")
        return False


# Main program
def main():
    print("PROJECT SHADOW - INTEGRATION HEALTH CHECK")
    print("-----------------------------------------")

    results = [
        check_rctf(),
        check_ps01(),
        check_research_archive(),
        check_ps02(),
        check_dns(),
        check_ssh()
    ]

    passed = sum(results)
    failed = len(results) - passed

    print("\n========== TEST SUMMARY ==========")
    print(f"Total Tests : {len(results)}")
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")

    if failed == 0:
        print("Overall     : ALL TESTS PASSED")
    else:
        print("Overall     : SOME TESTS FAILED")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

