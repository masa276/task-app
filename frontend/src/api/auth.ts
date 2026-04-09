import axios from "./client";

// --- 型定義 ---
export interface LoginData {
  email: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

// --- API 呼び出し ---

/**
 * ユーザーログイン
 * @param data {email, password}
 * @returns トークン情報 {access_token, token_type}
 */
export const loginUser = async (data: LoginData): Promise<TokenResponse> => {
  const response = await axios.post<TokenResponse>("/auth/login", data);
  return response.data;
};

/**
 * ログアウト処理（クライアント側のみ）
 */
export const logoutUser = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("token_type");
};

/**
 * 現在ログイン中のユーザーのアクセストークンを取得
 */
export const getAccessToken = (): string | null => {
  return localStorage.getItem("access_token");
};

/**
 * 認証ヘッダーを返す
 */
export const authHeader = (): { Authorization: string } | {} => {
  const token = getAccessToken();
  if (token) {
    return { Authorization: `Bearer ${token}` };
  } else {
    return {};
  }
};
