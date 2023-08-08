import React, { useState } from 'react';
import { Button, Form, Input } from 'antd';
import { LockOutlined, UserOutlined, MailOutlined } from '@ant-design/icons';
import "./form.css"

const Login = () => {
    const [register, setRegister] = useState(false)
    const registerClick = () => {
        setRegister(!register)
    }
    return(
        <div>
            <Form
                name="normal_login"
                className="login-form"
                initialValues={{
                    remember: true,
                }}
                >
                <Form.Item
                    name="username"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your Username!',
                    },
                    ]}
                >
                    <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" />
                </Form.Item>
                {register != false ? (<>
                    <Form.Item
                        name="Email"
                        rules={[
                        {
                            required: true,
                            message: 'Please input your Email!',
                        },
                        ]}
                    >
                        <Input prefix={<MailOutlined className="site-form-item-icon" />} placeholder="Email" />
                    </Form.Item>
                </>):<></>}
                <Form.Item
                    name="password"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your Password!',
                    },
                    ]}
                >
                    <Input.Password
                    prefix={<LockOutlined className="site-form-item-icon" />}
                    type="password"
                    placeholder="Password"
                    />
                </Form.Item>
                {register != true ? (<>
                    <Form.Item>
                        <a href="">
                            Forgot password ?
                        </a>
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="submit" className="login-form-button">
                            Log in
                        </Button>
                        Or <a onClick={registerClick}>register now!</a>
                    </Form.Item>
                </>):(<>
                    <Form.Item>
                        <Button type="primary" htmlType="submit" className="login-form-button">
                            Register
                        </Button>
                        Or <a onClick={registerClick}>Login now!</a>
                    </Form.Item>
                </>)}
            </Form>
        </div>
    )
}

export default Login;