import streamlit as st
import re

def generate_card_html(card_data, card_index):
    """個別のカードHTMLを生成"""
    # カードの色を交互に設定
    top_color = "#c7d2fe" if card_index % 2 == 1 else "#a5b4fc"
    
    return f'''
<!-- CARD {card_index} -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#ffffff;border:1px solid #e5e7eb;border-radius:12px;">
    <tbody><tr><td style="height:4px;background:{top_color};border-top-left-radius:12px;border-top-right-radius:12px;"></td></tr>
    <tr>
        <td style="padding:18px 20px 8px 20px;">
            <table role="presentation" width="100%">
                <tbody><tr>
                    <td style="white-space:nowrap;color:#475569;font:600 13px/1.4 Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;padding-right:10px;vertical-align:bottom;">{card_data['issue_number']}</td>
                    <td style="color:#0f172a;font:700 19px/1.4 Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">{card_data['title']}</td>
                </tr>
                </tbody></table>
        </td>
    </tr>
    <tr><td style="padding:6px 20px 0 20px;color:#64748b;font:600 13px/1 Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">コメント</td></tr>
    <tr>
        <td style="padding:10px 20px 6px 20px;">
            <table role="presentation" width="100%">
                <tbody><tr>
                    <td style="width:6px;background:#2563eb;"></td>
                    <td style="padding:8px 0 8px 12px;color:#334155;font:15px/1.8 Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">
                        💬 {card_data['comment']}
                    </td>
                </tr>
                </tbody></table>
        </td>
    </tr>
    <tr>
        <td style="padding:2px 20px 0 20px;">
            <table role="presentation">
                <tbody><tr>
                    <td align="center" style="width:40px;height:40px;background:#eef2f7;border-radius:20px;color:#64748b;font:700 18px/40px Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">{card_data['name_initial']}</td>
                    <td style="width:12px;"></td>
                    <td style="color:#0f172a;font:600 15px/1.3 Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">{card_data['name']}<br>
                        <span style="color:#64748b;font:12px/1.6 Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">{card_data['company']}</span>
                    </td>
                </tr>
                </tbody></table>
        </td>
    </tr>
    <tr>
        <td style="padding:12px 20px 18px 20px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tbody><tr>
                    <td style="background:#e8f0ff;border:1px solid #c7d2fe;border-radius:8px;">
                        <a href="{card_data['link']}" style="display:block;width:100%;text-align:center;color:#1d4ed8;text-decoration:none;font:700 15px/1 Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;padding:12px 18px;border-radius:8px;">
                            記事を読む
                        </a>
                    </td>
                </tr>
                </tbody></table>
        </td>
    </tr>
</tbody></table>
<div style="height:18px;line-height:18px;">&nbsp;</div>'''

def generate_full_html(delivery_date, cards):
    """完全なHTMLを生成"""
    cards_html = ""
    for i, card in enumerate(cards, 1):
        cards_html += generate_card_html(card, i)
    
    return f'''<meta charset="UTF-8">
<title>コメントクリップ（メール配信用・全幅ヘッダー＆横長ボタン）</title>
<!-- 100% wrapper -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0;padding:0;background:#f3f6fb;">
    <tbody><tr>
        <td align="center" style="padding:0;">
            <!-- ===== Header: full width background ===== -->
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#0b1b34;">
                <tbody><tr>
                    <td align="center" style="padding:0;">
                        <!-- inner fixed width -->
                        <table role="presentation" width="900" cellpadding="0" cellspacing="0" border="0" style="max-width:900px;width:100%;">
                            <tbody><tr>
                                <td style="padding:20px 24px 12px 24px;">
                                    <!-- row: badge + title -->
                                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                                        <tbody><tr>
                                            <td>
                                                <span style="display:inline-block;vertical-align:middle;background:#22315b;border:1px solid #2f3c66;color:#ffffff;font-weight:800;font-size:12px;letter-spacing:.04em;padding:7px 14px;border-radius:16px;font-family:Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">COMMENT CLIP</span>
                                                <span style="display:inline-block;vertical-align:middle;margin-left:12px;color:#ffffff;font-weight:800;font-size:22px;letter-spacing:.01em;font-family:Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">週刊 税務通信</span>
                                            </td>
                                        </tr>
                                        </tbody></table>
                                    <!-- row: date -->
                                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                                        <tbody><tr>
                                            <td style="padding-top:8px;color:#dbeafe;font-size:14px;font-family:Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">📅 {delivery_date}</td>
                                        </tr>
                                        </tbody></table>
                                    <!-- row: description -->
                                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                                        <tbody><tr>
                                            <td style="padding-top:6px;color:#c7d2fe;font-size:13px;line-height:1.7;font-family:Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">
                                                多様な視点からのコメントが記事を読むきっかけとなり、普段触れない分野への関心を広げます。また、記事やコメントを記憶に残し、後々の読み返しを促すことで読み忘れを防ぐことを目的としています。
                                            </td>
                                        </tr>
                                        </tbody></table>
                                </td>
                            </tr>
                            </tbody></table>
                    </td>
                </tr>
                </tbody></table>
            <!-- ===== /Header ===== -->
            
            <!-- ===== Body container ===== -->
            <table role="presentation" width="900" cellpadding="0" cellspacing="0" border="0" style="max-width:900px;width:100%;background:#f3f6fb;">
                <tbody><tr>
                    <td style="padding:24px;">
                        {cards_html}
                    </td>
                </tr>
                </tbody></table>
            <!-- ===== /Body ===== -->
            
            <!-- ===== Footer ===== -->
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#0b1b34;">
                <tbody><tr>
                    <td align="center" style="padding:18px 12px;">
                        <div style="color:#ffffff;font:12.5px/1.6 Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">
                            Copyright© 2016 Zeimu Kenkyukai, All rights reserved.
                        </div>
                        <div style="margin-top:8px;font-family:Arial,'Hiragino Kaku Gothic ProN',Meiryo,sans-serif;">
                            <a href="https://www.zeiken.co.jp/privacy/" style="color:#ffffff;text-decoration:none;margin:0 10px;">個人情報の保護について</a>
                            <a href="https://www.zeiken.co.jp/contact/request/" style="color:#ffffff;text-decoration:none;margin:0 10px;">お問い合わせ</a>
                        </div>
                    </td>
                </tr>
                </tbody></table>
            <!-- ===== /Footer ===== -->
        </td>
    </tr>
    </tbody></table>'''

def main():
    st.set_page_config(page_title="HTMLメールテンプレート生成", layout="wide")
    
    st.title("週刊税務通信 HTMLメールテンプレート生成")
    st.markdown("---")
    
    # サイドバーで基本設定
    with st.sidebar:
        st.header("基本設定")
        delivery_date = st.text_input("配信日", value="9月●日配信号")
        num_cards = st.number_input("記事数", min_value=1, max_value=20, value=7)
    
    # メイン部分で記事入力
    st.header("記事情報入力")
    
    cards = []
    cols = st.columns(2)
    
    for i in range(num_cards):
        with cols[i % 2]:
            with st.expander(f"記事 {i+1}", expanded=False):
                issue_number = st.text_input(f"号数", key=f"issue_{i}", value=f"第{3742+i}号")
                title = st.text_area(f"記事タイトル", key=f"title_{i}", height=80, value="")
                comment = st.text_area(f"コメント", key=f"comment_{i}", height=100, value="")
                name = st.text_input(f"コメンテーター名", key=f"name_{i}", value="")
                name_initial = st.text_input(f"名前の頭文字", key=f"initial_{i}", value="", max_chars=1)
                company = st.text_input(f"所属", key=f"company_{i}", value="")
                link = st.text_input(f"記事リンク", key=f"link_{i}", value=f"#article{i+1}")
                
                cards.append({
                    'issue_number': issue_number,
                    'title': title,
                    'comment': comment,
                    'name': name,
                    'name_initial': name_initial,
                    'company': company,
                    'link': link
                })
    
    st.markdown("---")
    
    # 生成ボタン
    if st.button("HTMLコード生成", type="primary"):
        if all(card['title'] and card['comment'] and card['name'] for card in cards):
            html_code = generate_full_html(delivery_date, cards)
            
            st.success("HTMLコードが生成されました！")
            
            # プレビューとコードを並べて表示
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("プレビュー")
                st.components.v1.html(html_code, height=800, scrolling=True)
            
            with col2:
                st.subheader("生成されたHTMLコード")
                st.code(html_code, language='html')
                
                # ダウンロードボタン
                st.download_button(
                    label="HTMLファイルをダウンロード",
                    data=html_code,
                    file_name=f"email_template_{delivery_date.replace('月', '').replace('日', '').replace('配信号', '')}.html",
                    mime="text/html"
                )
        else:
            st.error("すべての必須項目（タイトル、コメント、コメンテーター名）を入力してください。")
    
    # 使用方法の説明
    with st.expander("使用方法"):
        st.markdown("""
        ### 使用手順
        1. **基本設定**: サイドバーで配信日と記事数を設定
        2. **記事情報入力**: 各記事の詳細情報を入力
           - 号数: 記事の号数（例: 第3742号）
           - 記事タイトル: 記事のタイトル
           - コメント: コメンテーターのコメント（💬は自動で付きます）
           - コメンテーター名: コメントした人の名前
           - 名前の頭文字: アイコン表示用の文字（1文字）
           - 所属: コメンテーターの所属
           - 記事リンク: 記事へのリンクURL
        3. **生成**: 「HTMLコード生成」ボタンをクリック
        4. **確認・保存**: プレビューで確認後、HTMLファイルをダウンロード
        
        ### 注意事項
        - 記事数は1〜20件まで設定可能
        - すべての必須項目を入力してください
        - カードの色は自動で交互に設定されます
        """)

if __name__ == "__main__":
    main()