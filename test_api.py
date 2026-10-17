import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_success():
    """测试获取文章详情接口（正常路径）"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, f"预期状态码 200，实际为 {response.status_code}"
    data = response.json()
    assert "userId" in data, "响应体中缺失 userId 字段"
    assert "id" in data, "响应体中缺失 id 字段"
    assert data["id"] == 1, f"预期 id 为 1，实际为 {data['id']}"

def test_get_post_not_found():
    """测试获取不存在的文章（异常路径）"""
    response = requests.get(f"{BASE_URL}/posts/999999")
    # 实测发现接口返回 404，所以预期改为 404
    assert response.status_code == 404, f"预期状态码 404，实际为 {response.status_code}"
