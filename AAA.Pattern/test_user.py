from user import User

def test_user_profile_contains_name():
    # Arrange
    User = User(name="Chandan")

    # Act
    result = user.get_profile()

    # Assert
    assert "Chandan" in result