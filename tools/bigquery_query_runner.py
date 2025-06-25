# tools/bigquery_query_runner.py

from dify_plugin import Tool, ToolInvokeMessage

class BigQueryQueryRunnerTool(Tool):
    def _invoke(self) -> ToolInvokeMessage:
        # Difyから渡されたパラメータを取得します
        sql_query = self.tool_parameters.get('sql_query')
        if not sql_query:
            return self.create_error_message("SQL query is required.")

        # --- ここから下に、GCPの準備ができた後にAPI呼び出しコードを記述します ---

        # 今はダミーのメッセージを返します
        dummy_response = f"GCPの準備が完了したら、ここでクエリ '{sql_query}' を実行します。"

        # Difyにテキストメッセージとして結果を返します
        return self.create_text_message(dummy_response)
