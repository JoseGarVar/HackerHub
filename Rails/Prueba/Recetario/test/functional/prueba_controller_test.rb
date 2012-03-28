require 'test_helper'

class PruebaControllerTest < ActionController::TestCase
  test "should get index" do
    get :index
    assert_response :success
  end

  test "should get contactos" do
    get :contactos
    assert_response :success
  end

end
